"""
Node class for alpha beta pruning
Daniel Oh
"""
class AlphaBetaNode:
    """
    class for nodes in the alpha beta tree
    """
    def __init__(self, data, node_type):
        # all the attributes
        self.data = data
        self.children = []
        self.alpha = None
        self.beta = None
        self.following_nodes = [data]  # following nodes contain the root as well
        if (node_type.lower() != "min") and (node_type.lower() != "max"):  # invalid entry checking
            raise ValueError('type attribute in AlphaBetaNode object must be either "min" or "max"')
        else:
            self.node_type = node_type

    # inserts a child / appends to the child list
    def insert_child(self, input_child):
        self.children.append(input_child)


class AlphaBetaTree:
    """
    class for an alpha beta tree
    final leaf nodes are assumed to be of type int
    all other nodes are assumed to be of type str
    """
    def __init__(self, root_data, root_node_type):
        self.root = AlphaBetaNode(root_data, root_node_type)

    def insert(self, parent, child_data, child_type=None):
        if self.root.data == parent:  # if this node is the direct parent of the child we are adding
            if isinstance(child_data, int):  # if the end of the tree
                self.root.insert_child(child_data)
            else:  # if not the end of the tree
                new_tree = AlphaBetaTree(child_data, child_type)
                self.root.insert_child(new_tree)
                self.root.following_nodes.append(child_data)
        else:
            for i in range(len(self.root.children)):
                if parent in self.root.children[i].root.following_nodes:
                    self.root.following_nodes.append(child_data)  # add this
                    self.root.children[i].insert(parent, child_data, child_type)
                    break


def parse_input():
    """
    Takes the file and puts it in a more python friendly format
    :return: a list of the inputs

    The final list is of the following form:
    list = [[[('NodeName','MIN/MAX'), ... ,('NodeName','MIN/MAX')], [('NodeName', 'Child'), ... ,('NodeName', 'Child')]], [[('NodeName','MIN/MAX'), ... ,('NodeName','MIN/MAX')], [('NodeName', 'Child'), ... ,('NodeName', 'Child')]]]
                                                                                                                        ^ end of a line in the input file
    list[i] would give you [[('NodeName','MIN/MAX'), ... ,('NodeName','MIN/MAX')], [('NodeName', 'Child'), ... ,('NodeName', 'Child')]]
    list[i][0] would give you [('NodeName','MIN/MAX'), ... ,('NodeName','MIN/MAX')]
       list[i][0][j] would give you ('NodeName','MIN/MAX')
    list[i][1] would give you [('NodeName', 'Child'), ... ,('NodeName', 'Child')]
       list[i][1][j] would give you ('NodeName', 'Child')
    """
    with open("alphabeta.txt", 'r') as f_input:
        file_raw = [line for line in f_input.readlines()]
    file_text = [line[:-1] for line in file_raw[:-1]] + [file_raw[-1]]  # remove all '\n' characters
    file_text = [x.split(' ') for x in file_text]  # split each element on the space character; now it's a 2xn list
    for i in range(len(file_text)):  # split along '),(' and shave beginning and ending brackets
        file_text[i][0] = file_text[i][0][2:-2].split('),(')
        for j in range(len(file_text[i][0])):  # splitting tuples
            file_text[i][0][j] = file_text[i][0][j].split(',')

        file_text[i][1] = file_text[i][1][2:-2].split('),(')
        for k in range(len(file_text[i][1])):  # splitting tuples
            file_text[i][1][k] = file_text[i][1][k].split(',')

    # turn the numbers in the input into int type
    for i in range(len(file_text)):
        for j in range(len(file_text[i][1])):
            if is_int(file_text[i][1][j][1]):
                file_text[i][1][j][1] = int(file_text[i][1][j][1])

    tree_list = []
    # complexity is n^2 for one tree, n^3 for n trees
    for i in range(len(file_text)):
        tree = AlphaBetaTree(file_text[i][0][0][0], file_text[i][0][0][1])
        for j in range(len(file_text[i][1])):
            if isinstance(file_text[i][1][j][1], int):
                tree.insert(file_text[i][1][j][0], file_text[i][1][j][1])
            else:
                for k in range(len(file_text[i][0])):
                    if file_text[i][1][j][1] == file_text[i][0][k][0]:
                        tree.insert(file_text[i][1][j][0], file_text[i][1][j][1], file_text[i][0][j][1])
                        break
        tree_list.append(tree)
    return tree_list


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def TreeTest():
    test = AlphaBetaTree('A', 'MIN')
    test.insert('A', 'B', 'MAX')
    test.insert('A', 'C', 'MAX')
    test.insert('B', 19)
    # A->B->19
    print(test.root.children[0].root.children[0])  # should print 19
    # set alpha and beta of B to 7 and 8
    test.root.children[0].root.alpha = 7
    test.root.children[0].root.beta = 8
    print(test.root.children[0].root.data)  # should print B
    print(test.root.children[0].root.alpha)  # should print 7
    print(test.root.children[0].root.beta)  # should print 8
    print(test.root.children[0].root.node_type)  # should print MAX

    # testing a larger tree
    test2 = AlphaBetaTree('A', 'MIN')
    test2.insert('A', 'B', 'MAX')
    test2.insert('A', 'C', 'MAX')
    test2.insert('B', 'D', 'MIN')
    test2.insert('A', 'E', 'MAX')
    test2.insert('B', 'F', 'MIN')
    test2.insert('B', 'G', 'MIN')
    test2.insert('D', 20)
    test2.insert('D', 21)
    test2.insert('D', 22)
    print(test2.root.children[0].root.children[0].root.children[0])  # should print 20
    print(test2.root.children[0].root.children[0].root.children[1])  # should print 21
    print(test2.root.children[0].root.children[0].root.children[2])  # should print 22

    '''
    Explanation of AlphaBetaTree structure
    test.root will give you an AlphaBetaNode type meaning;
    test.root.data will give you the data/name of the node
    test.root.children[n] will give you the nth child
    say we had a tree that looked like:
                A
               / \
              B   C
             /
            19
    to get the AlphaBetaTree B, we do:
    test.root.children[0].root
    to access its data, we do:
    test.root.children[0].root.data
    
    to get 19, we do:
    test.root.children[0].root.children[0]
    this is because final leaves are stored directly in the children list
    '''


def main():
    pass


if __name__ == "__main__":
    testTreeList = parse_input()

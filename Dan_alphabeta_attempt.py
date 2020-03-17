"""
Node class for alpha beta pruning
Daniel Oh
"""


class AlphaBetaNode:
    """
    class for nodes in the alpha beta tree
    """
    def __init__(self, data, node_type, alpha, beta):
        # all the attributes
        self.data = data
        self.alpha = alpha
        self.beta = beta
        self.left_child = None
        self.right_child = None
        if (node_type.lower() != "min") and (node_type.lower() != "max"):  # invalid entry checking
            raise ValueError('type attribute in AlphaBetaNode object must be either "min" or "max"')

    # these functions are self explanatory; insert anything, including other nodes
    def insert_left_child(self, input_child):
        self.left_child = input_child

    def insert_right_child(self, input_child):
        self.right_child = input_child


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
            file_text[i][0][j] = tuple(file_text[i][0][j].split(','))

        file_text[i][1] = file_text[i][1][2:-2].split('),(')
        for k in range(len(file_text[i][1])):  # splitting tuples
            file_text[i][1][k] = tuple(file_text[i][1][k].split(','))

    return file_text


def main():
    parse_input()


if __name__ == "__main__":
    main()

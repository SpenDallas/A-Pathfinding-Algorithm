'''
Node class for alpha beta pruning
Daniel Oh
'''

class AlphaBetaNode:
    def __init__(self, data, node_type, alpha, beta):
        self.data = data
        self.alpha = alpha
        self.beta = beta
        self.left_child = None
        self.right_child = None
        print(node_type.lower())
        if (node_type.lower() != "min") and (node_type.lower() != "max"):
            raise ValueError('type parameter must be either "min" or "max"')

    def insert_left_child(self, input_child):
        self.left_child = input_child

    def insert_right_child(self, input_child):
        self.right_child = input_child


def main():
    testNode = AlphaBetaNode(7, "min", 5, 6)
    print(testNode.data)
    print(testNode.alpha)
    print(testNode.right_child)
    print(testNode.left_child)
    testNode2 = AlphaBetaNode(10, "max", 11, 12)
    testNode.insert_left_child(testNode2)
    print(testNode.left_child.data)


if __name__ == "__main__":
    main()
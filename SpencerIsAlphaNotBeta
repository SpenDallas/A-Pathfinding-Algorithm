import DanAttempt
INFINITY = 65535
nodesVisited = 0


def minimax(node, alpha, beta):

    global nodesVisited
    nodesVisited += 1

    if isinstance(node, int):
        return node

    if node.root.node_type == "MAX":
        bestVal = -INFINITY
        for child in node.root.children:
            value = minimax(child, alpha, beta)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    elif node.root.node_type == "MIN":
        bestVal = +INFINITY
        for child in node.root.children:
            value = minimax(child, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal
    else:
        print("Node not of type max or min. Please use valid node types")


if __name__ == "__main__":
    for tree in DanAttempt.parse_input():
        nodesVisited = 0
        print(minimax(tree, -INFINITY, INFINITY))
        print(nodesVisited)
        print()

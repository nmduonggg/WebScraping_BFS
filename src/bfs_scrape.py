from collections import deque
from get_child import get_child_nodes
from Node import Node
from read_and_write import add_to_file


def BFS(node: Node, results, outputFile):
    """
    Input: Starting node to search
    Output: All possible nodes including (move, value)
    """
    q = deque()
    visited = []
    q.append(node)
    visited.append(hashNode(node))

    while q:
        current_node = q.popleft()
        add_to_file(current_node, outputFile)
        children = get_child_nodes(current_node)

        # Print the depth - stop condition
        depth = len(current_node.move.strip().split('_')) - 1
        print(f"Running at depth {depth}")

        if depth == 3:
            if children == []:
                continue
            child = children[0]
            if hashNode(child) not in visited:
                q.append(child)
                visited.append(hashNode)

        elif depth == 4:
            continue
        
        else:
            for child in children:
                if hashNode(child) not in visited:
                    q.append(child)
                    visited.append(hashNode(child))



    return results

def hashNode(node: Node):
    """
    Input: Node(move, value, link)
    Remember that the same board posititons have the same evaluated value despite of
    their different combination of steps. Then instead of traversal of links which 
    will absolutely be unique, it is more efficient to traverse the position-related 
    hashed node.
    e.g: H8_G6_J7 and J7_G6_H8 will be the same (black - white - black)
    """

    moves = node.move.split("_")
    blackwhite = [1 if i%2 == 0 else 0 for i in  range(len(moves))]  ## 1 for black; 0 for white

    sorted_blacks = "_".join(sorted([moves[i] for i in range(len(moves)) if blackwhite[i] == 1]))
    sorted_whites = "_".join(sorted([moves[i] for i in range(len(moves)) if blackwhite[i] == 0]))

    return (sorted_blacks, sorted_whites)


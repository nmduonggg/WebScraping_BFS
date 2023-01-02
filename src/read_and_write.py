from Node import Node

def add_to_file(node: Node, outputFile: str):
    with open(outputFile, "a+") as file:
        file.write(f"{node.move} {node.value} \n")

def start_a_file(first_layer_node: Node, outputFile):
    with open(outputFile, "w") as f:
            f.write("---------Start--------- \n")
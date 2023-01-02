import Node
import get_child
import bfs_scrape
import read_and_write

def crawl_data(results: list):
    parent_node = Node.Node("", "", "/book/gomoku_15x15/")
    first_variations = get_child.get_child_nodes(parent_node)
    positions = dict()

    for first_layer_node in first_variations:
        file_path = f"file/position{first_layer_node.move}.txt"
        read_and_write.start_a_file(first_layer_node, file_path)
            
        children = bfs_scrape.BFS(first_layer_node, results, file_path)
        positions[first_layer_node] = children

    return positions


if __name__ == "__main__":
    results = []
    print(crawl_data(results))
    

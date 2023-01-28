from model.graph import Graph
from typing import List, Dict

class GraphController:

    def __init__(self, nodes: List[str], init_graph: List[Dict[str, Dict[str, int]]]) -> None:
        self.graph = Graph(nodes, init_graph)

    def get_path(self, previous_nodes:  Dict[str, str], start_node: str, target_node: str) -> List[str]:
        path = []
        node = target_node
        
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
    
        path.append(start_node)
        path.reverse()

        return path

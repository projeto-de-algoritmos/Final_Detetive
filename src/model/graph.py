import sys
from typing import List, Dict

class Graph(object):
    def __init__(self, nodes: List[str], init_graph: List[Dict[str, Dict[str, int]]]) -> None:
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes: List[str], init_graph: List[Dict[str, Dict[str, int]]]) -> Dict[str, Dict[str, int]]:
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self) -> None:
        return self.nodes
    
    def get_outgoing_edges(self, node: List[str]) -> None:
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1: str, node2: str) -> None:
        return self.graph[node1][node2]

    def dijkstra_algorithm(self, start_node):
        unvisited_nodes = list(self.get_nodes())
    
        shortest_path = {}
    
        previous_nodes = {}
    
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0
        
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            neighbors = self.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
    
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path

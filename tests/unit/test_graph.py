import sys 
sys.path.append("src/") 

from controller.file import FileController
from controller.graph import GraphController
import unittest

class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:
        pessoas_file = FileController('pessoas.csv', 'src/static/db/')
        nodes = pessoas_file.extract_nodes()

        graph_file = FileController('graph.csv', 'src/static/db/')
        init_graph = graph_file.extract_init_graph()
        self.controller = GraphController(nodes, init_graph)

    def test_previvous_nodes(self):
        expected_previous_nodes = {
            'Amanda': 'Jaimundo',
            'Anitta': 'Pedro',
            'Jaimundo': 'Maria',
            'Joao': 'Maria',
            'Leila': 'Matheus',
            'Matheus': 'Amanda',
            'Pedro': 'Jaimundo',
            'Suzana': 'Maria'
        }
        previous_nodes, _ = self.controller.graph.dijkstra_algorithm(start_node="Maria")
        self.assertEqual(expected_previous_nodes, previous_nodes)

    def test_shortest_path(self):
        expected_shortest_path = {
            'Amanda': 10,
            'Anitta': 20,
            'Jaimundo': 5,
            'Joao': 15,
            'Leila': 16,
            'Maria': 0,
            'Matheus': 11,
            'Pedro': 15,
            'Suzana': 10
        }
        _, shortest_path = self.controller.graph.dijkstra_algorithm(start_node="Maria")
        self.assertEqual(expected_shortest_path, shortest_path)

    def test_get_path(self):
        expected = ['Maria', 'Jaimundo', 'Amanda', 'Matheus']
        previous_nodes, _ = self.controller.graph.dijkstra_algorithm(start_node="Maria")
        path = self.controller.get_path(previous_nodes, start_node="Maria", target_node="Matheus")
        self.assertEqual(expected, path)

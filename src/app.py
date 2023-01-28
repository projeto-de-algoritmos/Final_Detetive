from controller.file import FileController
from controller.graph import GraphController

pessoas_file = FileController('pessoas.csv', 'src/static/db/')
nodes = pessoas_file.extract_nodes()
pessoas = pessoas_file.extract_pessoas()

graph_file = FileController('graph.csv', 'src/static/db/')
init_graph = graph_file.extract_init_graph()

controller = GraphController(nodes, init_graph)
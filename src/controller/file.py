from typing import List, Dict
import pandas as pd
from model.pessoa import Pessoa 

class FileController:
    def __init__(self, name: str, path: str = 'static/db/') -> None:
        self.path =  path + name
        self.df = pd.read_csv(self.path)

    def extract_nodes(self) -> List[str]:
        nodes = self.df['Nome'].tolist()
        return nodes

    def extract_init_graph(self) -> List[Dict[str, Dict[str, int]]]:
        init_graph = self.df.set_index('Destino').groupby('Origem').apply(lambda x: x.Peso.to_dict()).to_dict()
        return init_graph

    def extract_pessoas(self) -> List[Pessoa]:
        return [Pessoa(a.Nome, a.Relacao, a.Dna) for a in self.df.itertuples()]

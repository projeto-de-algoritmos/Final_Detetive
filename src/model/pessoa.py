from typing import List, Dict

class Pessoa(object):
    def __init__(self, nome: str, relacao: str, dna: str, saldacao: str, reacao: str, alibi: str, suspeito: str) -> None:
        self.nome = nome
        self.relacao = relacao
        self.dna = dna
        self.saldacao = saldacao
        self.reacao = reacao
        self.alibi = alibi
        self.suspeito = suspeito

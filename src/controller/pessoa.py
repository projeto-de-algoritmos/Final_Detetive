from model.pessoa import Pessoa
from .dna import DNAController

class PessoaController:
    def __init__(self, pessoa: Pessoa, dna: DNAController) -> None:
        self.dna = dna
        self.pessoa = pessoa
        self.preso = False
        print(f'[Detetive] Olá! {self.pessoa.nome}, como você está?')
        print(f'[{self.pessoa.nome}] {self.pessoa.saldacao}')
        print(f'[Detetive] Estou aqui pelo caso de Maria, que foi assassinada na noite passada na praça de São Carlos as 21h')
        print(f'[{self.pessoa.nome}] {self.pessoa.reacao}')
        self.acoes()

    def acoes(self) -> None:
        escolha = None
        while escolha != 6 and not self.preso:
            print("Escolha um a seguir:")
            print("<1> Qual a sua relação com a vitima?")
            print("<2> Onde estava na noite passada?")
            print("<3> Sabe quem pode ser um suspeito?")
            print("<4> Coletar amostra de DNA")
            print("<5> Prender")
            print("<6> Voltar")
            try:
                escolha = int(input())
                if (escolha < 1 or escolha > 6):
                    raise KeyError
                self.respostas(escolha)
            except:
                print("Precisa ser um número")

    def respostas(self, escolha: int) -> None:
        if escolha == 1:
            print(f'[{self.pessoa.nome}] {self.pessoa.relacao}')
        elif escolha == 2:
            print(f'[{self.pessoa.nome}] {self.pessoa.alibi}')
        elif escolha == 3:
            print(f'[{self.pessoa.nome}] {self.pessoa.suspeito}')
        elif escolha == 4:
            print(f'[Detetive] Compatibilidade com o DNA {self.dna.compara_dna(self.pessoa.dna)}%')
        elif escolha == 5:
            print(f'Você prendeu {self.pessoa.nome}.')
            self.preso = True

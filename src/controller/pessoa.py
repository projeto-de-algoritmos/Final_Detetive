from model.pessoa import Pessoa
from .dna import DNAController

from page.main import MainPage
from components.button import Button

class PessoaController:
    def __init__(self, pessoa: Pessoa, dna: DNAController, screen, pygame) -> None:
        self.dna = dna
        self.pessoa = pessoa
        self.preso = False
        self.screen = screen
        self.pygame = pygame 
        self.run = True
        self.main_page = MainPage(self.pygame, self.screen, text=f'[Detetive] Olá! {self.pessoa.nome}, como você está?')
        delay_time = 100
        last_key_check_time = 0
        text_appear = 0
        botoes_list = []
        while self.run:
            if text_appear <= 5:
                current_time = self.pygame.time.get_ticks()
                if current_time - last_key_check_time > delay_time:
                    keys = self.pygame.key.get_pressed()
                    if keys[self.pygame.K_RETURN]:
                        self.main_page.text.text = self.changetext(text_appear)
                        text_appear +=1
                    last_key_check_time = current_time
            else: 
                print('a fazer')

            self.clicked(botoes_list)
            self.main_page.update()
            self.pygame.display.update()
        # print(f'[Detetive] Olá! {self.pessoa.nome}, como você está?')
        # print(f'[{self.pessoa.nome}] {self.pessoa.saldacao}')
        # print(f'[Detetive] Estou aqui pelo caso de Maria, que foi assassinada na noite passada na praça de São Carlos as 21h')
        # print(f'[{self.pessoa.nome}] {self.pessoa.reacao}')
        # self.acoes()

    def acoes(self) -> None:
        escolha = None
        while escolha != 6 and not self.preso:
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

    def changetext(self, count: int) -> None:
        if count == 0:
            return(f'[Detetive] Olá! {self.pessoa.nome}, como você está?')
        elif count == 1:
            return(f'[{self.pessoa.nome}] {self.pessoa.saldacao}')
        elif count == 2:
            return(f'[Detetive] Estou aqui pelo caso de Maria')
        elif count == 3:
            return(f'[Detetive] Foi assassinada na noite passada na praça às 21h')
        elif count == 4:
            return(f'[{self.pessoa.nome}] {self.pessoa.reacao}')
        elif count == 5:
            return('Escolha um a seguir:')

    def clicked(self, botoes_list):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                raise SystemExit
            if event.type == self.pygame.MOUSEBUTTONUP:
                for b in botoes_list:
                    if b.button.collidepoint(event.pos):
                        pass

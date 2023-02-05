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
                botoes_list = [
                    Button('Qual a sua relação com a vitima?', pygame, screen, x = 30, button_width=100, font_size=20),
                    Button('Onde estava na noite passada?', pygame, screen, x = 100, font_size=20),
                    Button('Sabe quem pode ser um suspeito?', pygame, screen, x = 170, button_width=100, font_size=20),
                    Button('Coletar amostra de DNA', pygame, screen, x = 210, button_width=70, font_size=20),
                    Button('Prender', pygame, screen, x = 330, button_width=60, font_size=20),
                    Button('Voltar', pygame, screen, x = 400, button_width=60, font_size=20)
                ]
                

            self.main_page.update()
            for b in botoes_list:
                    b.update()
            self.clicked(botoes_list)
            self.pygame.display.update()

    def respostas(self, escolha: int) -> None:
        if escolha == 0:
            self.main_page.text.text = f'[{self.pessoa.nome}] {self.pessoa.relacao}'
        elif escolha == 1:
            self.main_page.text.text = f'[{self.pessoa.nome}] {self.pessoa.alibi}'
        elif escolha == 2:
            self.main_page.text.text = f'[{self.pessoa.nome}] {self.pessoa.suspeito}'
        elif escolha == 3:
            self.main_page.text.text = f'[Detetive] Compatibilidade com o DNA {self.dna.compara_dna(self.pessoa.dna)}%'
        elif escolha == 4:
            self.main_page.text.text = f'Você prendeu {self.pessoa.nome}.'
            self.preso = True
        elif escolha == 5:
            self.run = False

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
                for i, b in enumerate(botoes_list):
                    if b.button.collidepoint(event.pos):
                        self.respostas(i)

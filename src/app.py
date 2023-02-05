from controller.file import FileController
from controller.graph import GraphController
from controller.dna import DNAController
from controller.pessoa import PessoaController

from page.main import MainPage

from components.button import Button
import pygame

dna = DNAController()

pessoas_file = FileController('pessoas.csv', 'src/static/db/')
nodes = pessoas_file.extract_nodes()
pessoas = pessoas_file.extract_pessoas()

graph_file = FileController('graph.csv', 'src/static/db/')
init_graph = graph_file.extract_init_graph()

graph = GraphController(nodes, init_graph)
previous_nodes, shortest_path = graph.graph.dijkstra_algorithm(start_node="Maria")

visited_peoples = ['Maria']
option = ['Maria']

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("Dna Detective"))

main_page = MainPage(pygame, screen)
caso_em_aberto = False

botoes_list = []

delay_time = 100
last_key_check_time = 0
text_appear = 0
def clicked(botoes_list, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONUP:
            for b in botoes_list:
                if b.button.collidepoint(event.pos):
                    visited_peoples.append(b.text) if b.text not in visited_peoples else visited_peoples
                    caso_em_aberto = PessoaController(pessoas[b.text], dna, screen, pygame).preso

                    main_page.text.text = f'Perdendo amostra...'
                    dna.destroi_dna()


def game():
    global botoes_list, caso_em_aberto, main_page, screen, visited_peoples, option, delay_time, last_key_check_time, text_appear

    while caso_em_aberto != True:
        if text_appear <= 8:
            current_time = pygame.time.get_ticks()
            if current_time - last_key_check_time > delay_time:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    main_page.text.text = changetext(text_appear)
                    text_appear +=1
                last_key_check_time = current_time
        else: 
            for p in visited_peoples:
                for key in graph.graph.graph[p]:
                    option.append(key) if key not in option else option

            botoes_list = []
            for i, opt in enumerate(option):
                if i>0:
                    width = screen.get_width() / len(option)
                    b = Button(opt, pygame, screen, x = (i * width) - 50 , button_width = width - 10, font_size=int(width/ len(option) + 3))
                    botoes_list.append(b)

        main_page.update()

        for b in botoes_list:
            b.update()

        clicked(botoes_list, screen)
        pygame.display.update()


        # print(f'Fim de jogo')
        # print(f'Você fez a melhor rota!') if (visited_peoples == graph.get_path(previous_nodes, 
        #                                                                     start_node="Maria", 
        #                                                                     target_node="Matheus")
        #                                     )else print(f'Você demorou demais!')
        # print(f'Você descobriu o culpado!') if pessoa == "Matheus" else print(f'Você não achou o culpado!')

        # main_page.update()
        # # update display
        # pygame.display.update()

        
    pygame.quit()
    exit()

def changetext(count: int) -> None:
    if count == 0:
        return('Esse é um jogo de Investigação')
    elif count == 1:
        return('Você é um detetive que está investigando o caso de Maria')
    elif count == 2:
        return('Maria foi assassinada na noite passada na praça às 21h')
    elif count == 3:
        return('Na praça de São Carlos você encontrou o DNA do suspeito')
    elif count == 4:
        return('Agora basta você ter um suspeito para verificar o DNA')
    elif count == 5:
        return('Toda vez que você compara o DNA você perde um pouco ')
    elif count == 6:
        return('compare com sabedoria')
    elif count == 7:
        return('E a cada entrevista também! Então tome cuidado')
    elif count == 8:
        return('Escolha alguem para entrevistar!')

if __name__ == "__main__":
    game()

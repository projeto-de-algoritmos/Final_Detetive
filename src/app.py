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

def clicked(botoes_list):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONUP:
            for b in botoes_list:
                if b.button.collidepoint(event.pos):
                    b.action()


def game():
    pygame.init()

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption(("Dna Detective"))

    main_page = MainPage(pygame, screen)

    botoes_list = []

    delay_time = 100
    last_key_check_time = 0
    text_appear = 0
    run = True
    while run:

        clicked(botoes_list)
        
        main_page.update()

        current_time = pygame.time.get_ticks()
        if current_time - last_key_check_time > delay_time:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                main_page.text = changetext(text_appear)
                text_appear +=1
            last_key_check_time = current_time
        
        for b in botoes_list:
            b.update()

        # update display
        pygame.display.update()
        
    pygame.quit()
    exit()

def menu_escolha() -> None:
    caso_em_aberto = False
    pessoa = None
    while caso_em_aberto != True:
        text = (f'*******************************\nEscolha alguem para entrevistar!')
        for p in visited_peoples:
            for key in graph.graph.graph[p]:
                option.append(key) if key not in option else option
        
        for i, opt in enumerate(option):
            if i>0:
                print(f'[{i}] {opt}')
        print(f'[{len(option)}] Sair')

        try:
            escolha = int(input())
            if (escolha < 0 or escolha > len(option)):
                raise KeyError
            elif (escolha==len(option)):
                caso_em_aberto = True
                break
            visited_peoples.append(option[escolha]) if option[escolha] not in visited_peoples else visited_peoples
            caso_em_aberto = PessoaController(pessoas[option[escolha]], dna).preso

            print(f'Perdendo amostra...')
            dna.destroi_dna()
            pessoa = option[escolha]
        except:
            print("Precisa ser um número")

    print(f'*******************************')
    print(f'Fim de jogo')
    print(f'Você fez a melhor rota!') if (visited_peoples == graph.get_path(previous_nodes, 
                                                                           start_node="Maria", 
                                                                           target_node="Matheus")
                                        )else print(f'Você demorou demais!')
    print(f'Você descobriu o culpado!') if pessoa == "Matheus" else print(f'Você não achou o culpado!')

def changetext( count : int) -> None:
    if count == 0:
        return('Bem vindo!')
    elif count == 1:
        return('Esse é um jogo de Investigação')
    elif count == 2:
        return('Você é um detetive que está investigando o caso de Maria')
    elif count == 3:
        return('Maria foi assassinada na noite passada na praça de São Carlos as 21h')
    elif count == 4:
        return('Na praça de São Carlos você encontrou o DNA do suspeito')
    elif count == 5:
        return('Agora basta você encontrar um suspeito para verificar o DNA')
    elif count == 6:
        return('Mas cuidado! Toda vez que você compara o DNA você perde um pouco compare com sabedoria')
    elif count == 7:
        return('E a cada entrevista também! Então tome cuidado')

if __name__ == "__main__":
    game()

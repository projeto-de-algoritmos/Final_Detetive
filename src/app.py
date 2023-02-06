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

delay_time = 150
last_key_check_time = 0
text_appear = 0
hacker = 1

def clicked(botoes_list, screen):
    global hacker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONUP:
            for b in botoes_list:
                if b.button.collidepoint(event.pos):
                    suspeito = PessoaController(pessoas[b.text], dna, screen, pygame)
                    caso_em_aberto = suspeito.preso
                    visited_peoples.append(b.text) if b.text not in visited_peoples else visited_peoples
                    if(caso_em_aberto != True):
                        main_page.text.text = f'Perdendo amostra...'
                        dna.destroi_dna()
                    else:
                        endgame(suspeito)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_h]:
                    hacker = 0

def game():
    global hacker,botoes_list, caso_em_aberto, main_page, screen, visited_peoples, option, delay_time, last_key_check_time, text_appear

    while caso_em_aberto != True:
        if text_appear <= 8:
            current_time = pygame.time.get_ticks()
            if current_time - last_key_check_time > delay_time:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    main_page.text.text = changetext(text_appear)
                    text_appear +=1
                last_key_check_time = current_time
        else: 
            for p in visited_peoples:
                for key in graph.graph.graph[p]:
                    option.append(key) if key not in option else option
            
            botoes_list = []
            for i, opt in enumerate(option):
                if i>=hacker:
                    width = screen.get_width() / len(option)
                    b = Button(opt, 
                               pygame, 
                               screen, 
                               x = (i * width) - 50 , 
                               button_width = width - 10, 
                               font_size=int(width/ len(option) + 3)
                               )
                    botoes_list.append(b)
        main_page.portrait = "assets/None.png"
        main_page.update()

        for b in botoes_list:
            b.update()

        clicked(botoes_list, screen)
        pygame.display.update()
    pygame.quit()
    exit()

def endgame(preso : PessoaController):
    easter_egg = False
    main_page.text.text = f'Fim de jogo'
    if (preso.pessoa.nome == "Matheus"):
        text_resultado = f'Você descobriu o culpado!'
        botao_end = Button(f'Parabens',pygame,screen, 125,40,460,250,30)
        easter_egg = True
        if (visited_peoples == graph.get_path(previous_nodes,start_node="Maria",target_node="Matheus")):
            text_speed = f'Você fez a melhor rota!'
        else:
            text_speed = f'Você demorou demais!'

    else:
        text_resultado = f'Você não achou o culpado!'
        text_speed = f''
        botao_end = Button(f'Tentar novamente',pygame,screen, 125,40,460,250,30)

    font = pygame.font.Font(None, 36)
    text_resultado_image = font.render(text_resultado, True, (255, 255, 255))
    text_speed_image = font.render(text_speed, True, (255, 255, 255))
    #Rect(left, top, width, height) -
    text_resultado_box = pygame.Rect(100, 260, 200, 50)
    text_speed_box = pygame.Rect(120, 300, 200, 50)
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
            if event.type == pygame.MOUSEBUTTONUP:
                if easter_egg == True:
                    pygame.quit()
                    raise SystemExit
                game()
       
        main_page.update()

        screen.blit(text_resultado_image, text_resultado_box)
        screen.blit(text_speed_image, text_speed_box)
        botao_end.update()
        pygame.display.update()
    
    pygame.quit()
    exit()

    ...

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
        return('Escolha um suspeito para interrogar!')

if __name__ == "__main__":
    game()

from controller.file import FileController
from controller.graph import GraphController
from controller.dna import DNAController
from controller.pessoa import PessoaController
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

def game():
    pygame.init()
    
    screen = pygame.display.set_mode((500,500))
    
    pygame.display.set_caption(("Dna Detective"))
    font = pygame.font.Font(None, 28)
    # create a rect object for the text box

    text_padding = 10
    text_box = pygame.Rect(0, screen.get_height() - 150, 500, 150)
    text_rect = pygame.Rect(text_box.left + text_padding, 
                            text_box.top + text_padding, 
                            text_box.width - 2 * text_padding, 
                            text_box.height - 2 * text_padding)
    color_box = pygame.Surface((text_box.width, text_box.height))
    color_box.fill((88, 90, 219))
    color_box.set_alpha(95) 
    # Botões
    text = ""
    button_width = 130
    button_height = 40
    button_padding = 100
    button1 = pygame.Rect(button_padding, 
                          screen.get_height() - button_height - 5, 
                          button_width, 
                          button_height)
    button2 = pygame.Rect(button_padding + button_width + 50,  
                          screen.get_height() - button_height - 5, 
                          button_width, 
                          button_height)
    button1_text = "Prender!"
    button2_text = "Coletar DNA"
    button1_text_image = font.render(button1_text, True, (255, 255, 255))
    button2_text_image = font.render(button2_text, True, (255, 255, 255))

    background_image = pygame.image.load("assets/Interrogation_room.png")
    delay_time = 100
    last_key_check_time = 0
    text_appear = 0
    run = True
    while run:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
            # detect button clicks
                if button1.collidepoint(event.pos):
                    print("Button 1 clicked")
                if button2.collidepoint(event.pos):
                    print("Button 2 clicked")
        
        screen.blit(background_image, (0, 0))

        if current_time - last_key_check_time > delay_time:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                text = changetext(text_appear)
                text_appear +=1
            last_key_check_time = current_time

        text_image = create_wrapped_text_surface(text,font.render(text, True, (255, 255, 255)) )
        screen.blit(color_box, text_box)
        screen.blit(text_image, text_rect)
        
        #Botões fixos
        pygame.draw.rect(screen, (73, 75, 222), button1)
        pygame.draw.rect(screen, (73, 75, 222), button2)
        screen.blit(button1_text_image, 
                    (button1.left + button_width // 2 - button1_text_image.get_width() // 2, 
                     button1.top + button_height // 2 - button1_text_image.get_height() // 2))
        screen.blit(button2_text_image, 
                    (button2.left + button_width // 2 - button2_text_image.get_width() // 2, 
                     button2.top + button_height // 2 - button2_text_image.get_height() // 2))

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
def create_wrapped_text_surface(text, 
                                text_surface,
                                font_size=28, 
                                font_color=(255, 255, 255)):
    pos = [20,350]
    font = pygame.font.Font(None, font_size)
    words = [word.split(' ') for word in text]
    space = font.size(' ')[0]
    max_width = 50
    x,y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, font_color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            text_surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
   
    return text_surface

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


from controller.file import FileController
from controller.graph import GraphController
from controller.dna import DNAController
from controller.pessoa import PessoaController

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

def menu_escolha() -> None:
    caso_em_aberto = False
    pessoa = None
    while caso_em_aberto != True:
        print(f'*******************************')
        print(f'Escolha alguem para entrevistar!')
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
    print(f'Você fez a melhor rota!') if visited_peoples == graph.get_path(previous_nodes, start_node="Maria", target_node="Matheus") else print(f'Você demorou demais!')
    print(f'Você descobriu o culpado!') if pessoa == "Matheus" else print(f'Você não achou o culpado!')

def menu_inicial() -> None:
    print(f'Bem vindo!')
    print(f'Esse é um jogo de Ingestigação')
    print(f'Você é um detetive que está investigando o caso de Maria')
    print(f'Maria foi assassinada na noite passada na praça de São Carlos as 21h')
    print(f'Na praça de São Carlos você encontrou o DNA do suspeito')
    print(f'Agora basta você encontrar um suspeito para verificar o DNA')
    print(f'Mas cuidado! Toda vez que você compara o DNA você perde um pouco, compare com sabedoria')
    print(f'E a cada entrevista também! Então tome cuidado')
    menu_escolha()

if __name__ == "__main__":
    menu_inicial()

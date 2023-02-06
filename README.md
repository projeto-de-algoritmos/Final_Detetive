# Detetive

**Número da Lista**: 26<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0011267  |  Giovanna Borges Bottino        |
| 18/0119818  |  Felipe Boccardi Silva Agustini |

## Sobre 
Esse projeto é um jogo de Investigação. Você irá jogar como um detetive investigando um crime. Para isso há um grafo que contém nodes pessoas e uma amostra de dna. A cada vez que avança na investigação você recebe mais conexões e vai perdendo a amostra de dna usada para encontrar o criminoso. O Dna é analisado usando o algoritimo de alinhamento de sequencia.

## Screenshots
![imagem 1](/public/1.PNG)

![imagem 2](/public/2.PNG)

![imagem 3](/public/3.PNG)

![imagem 4](/public/4.PNG)

## Video

https://user-images.githubusercontent.com/23579166/217007559-e90498ff-5e7a-4690-a1b6-9b4bea7f085a.mp4

## Instalação 
*Linguagem*: Python<br>
*Framework*: <br>

### Crie um ambiente em python 3
```
python3 -m venv env
```

### Ative o ambiente
```
source env/bin/activate
```
ou se estiver usando windows

```
.\env\Scripts\activate
```
### Instale as dependencias
```
pip install -r requirements.txt
```

## Testes 

Para rodar os testes basta executar o comando a baixo.
```
python -m unittest discover tests/unit/
```

## Uso 
Basta executar o arquivo `app.py`. 
```
python src/app.py
```
Utilize o mouse para clicar nos botões e a tecla enter ou a barra de espaço para passar os dialogos.

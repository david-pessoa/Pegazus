#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
import pandas as pd 

response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

produtos = [] # Lista para armazenar os nomes dos produtos com preço maior que 30
for loja in response: 
    
    for produto in loja["produtos"]: #Para cada loja, será avaliado cada produto nela

        if produto["preço"] > 30: # Se o preço do produto é maior que 30, então adiciona seu nome na lista
            produtos.append(produto["nome"])

print("Produtos com preço maior que 30:", produtos) #Imprime

#Descrição da resolução:
#Como as lojas estão dentro de uma lista, posso iterar entre elas com o laço for,
#Cada loja é representada por um dicionário, então basta acessar os produtos escrevendo: loja["produtos"]
#Os produtos por sua vez, estão numa lista, então podemos iterá-los num segundo laço for aninhado
#Cada produto é representado por um dicionário, então basta acessar seu preço escrevendo: produto["preço"]

#Sendo assim, posso dizer que adotei essa forma por ser mais intuitiva, do que tentar utilizar a biblioteca pandas por exemplo



#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}
lista_produtos = responsejson["produtos"] #Obtém lista com os produtos da loja

precoB = 0 #Coloca o preço de B como 0

for produto in lista_produtos: #Para cada produto na lista,
    if produto["nome"] == "Produto B": #Verifica se o nome é "Produto B"
        precoB = produto["preço"] #Pega o preço e interrompe a busca
        break

if precoB == 0: #Se não encontrar nenhum produtoB
    print("Produto B não foi encontrado")

print("Preço do produto B:", precoB)

#Decidi utilizar esta solução, pois ela é a mesma estratégia utilizada no exercício anterior.
#Logo, também é mais intuitiva além de já estar mais acostumado.

#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def QuickSort(vetor, inicio = 0, fim = None):
    if fim is None:
        fim = len(vetor) - 1
    if inicio < fim:
        pivot_pos = partition(vetor, inicio, fim)
        QuickSort(vetor, inicio, pivot_pos - 1)
        QuickSort(vetor, pivot_pos + 1, fim)
    return vetor

lista_ordenada = QuickSort(lista)
print("Lista ordenada:", lista_ordenada)





#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]


#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra


#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO


#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta









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


#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

def Merge(inicio, fim, meio, vetor):
    left = vetor[inicio:meio] #Divide o vetor em duas partes (left, right)
    right = vetor[meio:fim]
    top_left, top_right = 0, 0 #Variáveis para varrer cada partes do menor ao maior número
    #O topo é o menor número de cada sublista, portanto

    for k in range(inicio, fim): #Para cada posição k no vetor:

        if top_left >= len(left): #Se todos os números de left já foram inseridos no vetor
            vetor[k] = right[top_right] #Coloca o número no topo de right no vetor
            top_right += 1

        elif top_right >= len(right): #Se todos os números de right já foram inseridos no vetor
            vetor[k] = left[top_left] #Coloca o número no topo de letf no vetor
            top_left += 1
        
        elif right[top_right] > left[top_left]: #Se left possui o menor topo
            vetor[k] = left[top_left] #Coloca o número no topo de left no vetor
            top_left += 1 

        else: #Se right possui o menor topo
            vetor[k] = right[top_right] #Coloca o número no topo de right no vetor
            top_right += 1

    return vetor #Retorna vetor ordenado
      
def MergeSort(vetor, inicio, fim):
    if fim - inicio > 1: # Se a sublista contém mais de um elemento:
        meio = (inicio + fim) // 2 #Calcula o índice no meio da lista
        MergeSort(vetor, meio, fim) # Divide a lista em duas e aplica o MergeSort recursivamente para as duas partes
        MergeSort(vetor, inicio, meio)
        return Merge(inicio, fim, meio, vetor) #Junta as sublistas ordenadas
    else:
        return vetor #Se a sublista contém apenas um elemento retorna a sublista e encerra a recursão

def StartMerge(vetor): #Obtém primeiro e último índices da lista para poder passá-los 
    fim = len(vetor)   #como argumento para a função principal
    inicio = 0
    return MergeSort(vetor, inicio, fim)

lista_ordenada = StartMerge(lista)
print("Lista ordenada:", lista_ordenada)


#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]
new_list = []

for item in lista:
    new_list.append(item.strip()) # Para cada string da lista, adiciona sua versão sem espaços em branco

print("Lista sem espaços em branco:", new_list)

#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

nova_lista = lista[0:1] + lista[2:] #Elimina o segundo item dividindo a lista em duas partes e concatenando-as

print("Lista sem o segundo elemento:", nova_lista)

#6-substitua todos os "joao" da lista por "maria"

lista_nomes = ["joao", "ana", "joana","joao", "ricardo", "joao"]

for i in range(len(lista_nomes)):
    if lista_nomes[i] == "joao":
        lista_nomes[i] = "maria"

print("Lista com o nome 'joao' substituído por 'maria':", nova_lista)


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









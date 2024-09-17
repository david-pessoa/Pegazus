# Explicações das soluções dos algoritmos

## Exercício 1
Descrição da resolução:
Como as lojas estão dentro de uma lista, posso iterar entre elas com o laço for. cada loja é representada por um dicionário, então basta acessar os produtos escrevendo: `loja["produtos"]`. Os produtos por sua vez, estão numa lista, então podemos iterá-los num segundo laço for aninhado. Cada produto é representado por um dicionário, então basta acessar seu preço escrevendo: `produto["preço"]`. Sendo assim, posso dizer que adotei essa forma por ser mais intuitiva, do que tentar utilizar a biblioteca pandas por exemplo.

## Exercício 2
Decidi utilizar esta solução, pois ela é a mesma estratégia utilizada no exercício anterior. Logo, também é mais intuitiva além de já estar mais acostumado.

## Exercício 3
Escolhi o algoritmo MergeSort como método de ordenação, pois ele é mais veloz, possuindo complexidade O(n log n) tanto em seu pior caso quanto em seu melhor caso. Diferentemente do Quicksort, que, apesar de possuir a mesma complexidade, em seu pior caso apresenta complexidade O(n ^ 2).

## Exercício 7
Utilizei esta solução, por ser mais intuitiva e também porque é a maneira mais utilizada. Como é costume para muitas pessoas, a variável usada para varrer o vetor foi nomeada `i`. Já a condição imposta no loop para parada foi: `lista_while[i] <= 5`, assim não é necessário usar um `if` ou `break`, já que esta condição é suficiente para parar o código quando necessário.

## Exercício 8
Utilizei esta solução, pois, primeiro necessitava obter os dados através da API por meio de uma requisição GET HTTP. Não poderia ser uma requisição do tipo POST, por exemplo, já que o intuito não é enviar dados para o servidor e sim obter dados dele. Então, utilizei a função `get()` da biblioteca `requests` para obter a resposta do servidor e depois extrair o json com os dados. Após isso, precisei apenas acessar os dados iterando a lista `dados`. Para cada task, era verificado o valor correspondente à chave `completed`, se fosse igual a True, era contada como completa, caso contrário como pendente.

## Exercício 9
Utilizei a mesma forma para obter os dados através da API pelos mesmos motivos citados no exercício anterior. Já para o parsing dos dados, decidi que a melhor forma seria guardar as pessoas e suas informações num dicionário, sendo a chave os nomes das pessoas. Poderia ter usado o ID, mas o enunciado não permitiu. As outras informações sobre cada pessoa ficaram numa lista, que constituía o valor da chave no dicionário. Preferi uma lista do que outro dicionário para melhorar a legibilidade do código e seu entendimento.

# Desafio
Este desafio foi feito utilizando dois arquivos: o `cliente.py`, contendo a classe `Cliente()` para criar objetos representando cada cliente cadastrado no sistema, e o `Desafio.py`, contendo o restante do código com os códigos de cada tela.

## Classe `Cliente`
### Atributos
* `id`: contém o ID do cliente (int)
* `nome`: contém o nome do cliente (string)
* `cpf`: contém o CPF do cliente (string)
* `senha`: contém a senha da conta do cliente (string)
* `saldo`: contém o saldo inicial do cliente. Inicia com 0 (float)

### Métodos
* `saque()`: Parâmetro: `dinheiro` (float), Retorna vazio. Função: subtrai o valor de `dinheiro` do atributo `saldo`
* `deposito()`: Parâmetro: `dinheiro` (float), Retorna vazio. Função: adiciona o valor de `dinheiro` do atributo `saldo`
* `setSenha()`: Parâmetro: `senha` (string), Retorna vazio. Função: define o valor do atributo `senha` como o valor do parâmetro `senha`
* `getId()`: Parâmetros: Nenhum, Retorna o valor do atributo `id`
* `getNome()`: Parâmetros: Nenhum, Retorna o valor do atributo `nome`
* `getCPF()`: Parâmetros: Nenhum, Retorna o valor do atributo `cpf`
* `getSenha()`: Parâmetros: Nenhum, Retorna o valor do atributo `senha`
* `getSaldo()`: Parâmetros: Nenhum, Retorna o valor do atributo `slado`

## `Desafio.py`
### Sobre as telas da interface gráfica
Para realizar o desafio, utilizei o módulo tkinter do python para criar interfaces gráficas. As telas seguem um padrão: todas com fundo roxo, título da tela sempre em branco, demais textos em preto, botões em amarelo em teoria* e, por fim, erros em vermelho. Como os botões são utilizados para direcionar o usuário de uma tela para outra, foi necessário representar cada tela por uma função, para que o argumento `command` do construtor da classe `Button` receba a essa função criada. Por exemplo, o botão "Cadastre-se" da tela inicial recebe em seu `command` a função `tela_cadastro()`. Também é importante destacar que a cada mudança de tela, a janela anterior criada é destruída pelo método `destroy()` da classe `Tk`, para que o usuário não fique com múltiplas janelas abertas. Pois, a cada mudança de tela na realidade, uma nova janela é criada.
  
  Quanto aos clientes, foi criada a variável global `cliente_logado` para armazenar o objeto do cliente logado na aplicação e o dicionário `clientes` para armazenar todos os clientes cadastrados. O dicionário contém como chave o `id` do cliente e como valor o objeto da classe `Cliente` com esse `id`.

### Tela Inicial
Inicialmente, é chamada a função tela_inicial(), em que é exibido o título "Banco do python". Junto a caixas de entrada de texto e textos exigindo a entrada dos dados cadastrais do usuário: CPF e senha da conta. Abaixo, é possível encontrar os botões "Cadastre-se" e "Login". Caso o usuário tente logar, mas não esteja cadastrado ou não haja nenhum usuário salvo, será exibida uma mensagem de erro, caso contrário é direcionado para a tela de mostra saldo. Se ele clicar em cadastre-se, será exibida a tela de cadastro.

*OBS: Eu elaborei este código no MacOS, então é possível que ele apresente um comportamento diferente quando executado no Windows

<img width="841" alt="Tela Inicial" src="https://github.com/user-attachments/assets/2148947f-174b-4bba-a121-e719905b7e81">

### Tela de Cadastro
A tela de cadastro possui textos e caixas de entrada solicitando a entrada de: nome, CPF e senha para a conta. Ao fim, possui o botão "Cadastrar" para finalizar o cadastro.

<img width="844" alt="Tela de Cadastro" src="https://github.com/user-attachments/assets/2deba2bf-1ecb-4721-a061-d0cdf7e077f3">

### Tela de Mostar o Saldo
A tela de mostrar o saldo inicialmente verifica se o cliente é um cliente que acabou de se cadastrar. Caso seja, salva as suas informações digitadas na tela de cadastro. Se a pessoa acabou de realizar um depósito, o valor do depósito é adicionado ao saldo do cliente. Depois disso, a tela é carregada, exibindo o título: "Bem vindo, {nome do cliente}". No centro da tela, é indicado o saldo atual do cliente e abaixo os botões com as opções de realizar saque ou depósito na conta.

<img width="837" alt="Tela Mostra Saldo" src="https://github.com/user-attachments/assets/c5789ebb-0da2-4415-b54c-bafdd723c6d3">

### Tela para realizar saques
A tela para realizar saques exibe uma entrada, para que o usuário digite o valor em reais que deseja sacar e um botão abaixo para confirmar o saque. Caso o valor do saque exceda o valor do saldo, é exibida uma mensagem de erro, exibindo o valor atual do saldo. Senão, o saque é realizado com sucesso e o usuário retorna para a tela de mostrar o saldo.

<img width="847" alt="Tela Saque" src="https://github.com/user-attachments/assets/3afcb9a5-a9e4-4a61-8871-8980ea10ea6e">

### Tela para realizar depósitos
A tela para realizar depósitos exibe uma entrada, para que o usuário digite o valor em reais que deseja depositar e um botão abaixo para confirmar o depósito. Após realizar o depósito, o usuário retorna para a tela Mostra Saldo

<img width="847" alt="Tela deposito" src="https://github.com/user-attachments/assets/020e31fa-a3d3-47b9-b44f-75691fe4afc6">

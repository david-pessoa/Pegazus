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
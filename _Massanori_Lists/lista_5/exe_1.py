# Explicando um pseudo código


# Definindo os valores das variaveis x e y

x = 2
y = 5

# Agora vamos para o teste lógico utilizando os valores definidos nas variaveis

# Nesta primeira condição verificamos se o valor de "y" é maior que 8, e caso a afirmação seja verdade, o y receberá o valor de y * 2

se y > 8 então
	y = y * 2

# Já aqui na condição de caso contrario, o x irá assumir o valor de x * 2
caso contrario,
	x = x * 2

#Por fim há a impressão do valor de x+y
imprime (x + y)

'''
Algoritimo explicado acima, linha a linha, trabalha utilizando testes/condições, abaixo vou fazer uma explicação por extenso do algoritmo

Ao iniciar o algoritimo são definidas duas variaveis, estas 'x' e 'y', que recebem 2 e 5 respectivamente. Depois deste há um teste de condições, onde num primeiro momento é verificado se o valor colocado em y é maior que 8, se a condição se mostrar verdadeira, o algoritmo fará com que o y receba o resultado de y * 2, resultando numa expressão igual a esta, y = y * 2.

A proxima verificação é feira pelo algoritmo caso a primeira verificação seja falsa, assim fazendo com que a segunda verificação seja ativada, já que esta funciona de maneira que caso a primeira não seja ativada, use a segunda (caso contrario), ao ativar esta função o valor de x recebera o resultado de x * 2, este que se usa a expressão igual a esta, x = x * 2

Por fim depois de passar por todos os testes, e realizar os calculos, o algoritmo irá imprimir os valores de x + y

Pronto este é nosso algoritmo

Em nosso caso o valor de y é menor que 8 o que ativa a segunda verificação que faz x = x * 2, ou seja x = 4, e na hora da impressão juntado os valores de 'x' e 'y', ou seja x = 4 + y = 5, resultando em 9

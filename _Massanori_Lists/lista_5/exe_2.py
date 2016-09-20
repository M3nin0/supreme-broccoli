# Exe 2 - Quantas vezes são impresos o 'OI'


# No algoritmo abaixo é feito um laço dentro do outro
# Veja:

# Nesta primeira linha, nos é mostrado que o valor de "i" vai de 1 até 9, ou seja ele irá iniciar o laço e quando terminar vai ser acrerido a ele mesmo mais um valor, e assim iŕa ser feito até chegar no numero 9
para i = 1 até 9 
	# Já aqui é feita uma outra verificação, se o valor de "i" é diferente de 3, e caso seja verdade, ele irá executar os lanços seguintes, caso seja falso, nada será feito 
	se i != 3, então
		# Aqui já estamos dentro do laço que será ativado caso o valor de 'i' seja diferente de 3, 
		# neste é feito um outro loop onde o valor de 'j' ira de 1 até 6, e enquanto o valor de 'j' estiver dentro dos valores de 1 a 6, será impresso 'oi'
		para j = 1 até 6
			imprime 'oi'

'''

Veja que este algoritmo é bem mais elaborado que o anterior, aqui explicarei por extenso como ele funciona:

Em seu inicio é gerado um laço que irá se repetir de 1 até 9, esta repetição gera um valor, que sempre será atribuido a variavel 'i', depois que o laço se inicia é feito uma verificação, para saber se o valor de i, é diferente de 3, caso seja diferente, ele irá executar outros comandos que estão subjacentes a ele, que neste caso será um outro laço, que irá realizar 6 repetições, e cada vez que ele repetir, será feito a impressão da palavra 'oi' na tela. Ele fará a impressão de 48 'oi' na tela, mas porque não 54,já que o  primeiro laço se repete 9 vezes e o segundo 6 vezes. Este valor não condiz com a realidade pois há a condição de verificação, que verifica se o valor de 'i' é diferente de 3, em uma das vezes o valor de 'i' é igual a tres, o que ocasiona não execução dos comandos adjacentes a condição quando verdadeira, fazendo assim que a execução seja feita 9 vezes, mas executando o laço dos 6 'oi' na tela apenas 8 vezes, o que resulta em 48
'''

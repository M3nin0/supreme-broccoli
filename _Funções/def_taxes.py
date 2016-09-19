'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o 
custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas'''

def somaImposto(taxaImposto, custo):
	total = ((taxaImposto * custo) / 100) + custo
	print("O produto antes dos impostos custavam", custo)
	print("Agora passou a custar", total)

taxaImposto = int(input("Insira a porcentagem de taxas a serem adicionados: "))
custo = int(input("Insira o valor do produto que está sendo taxado: "))

somaImposto(taxaImposto,custo)
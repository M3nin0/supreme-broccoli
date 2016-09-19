# Devolvendo numeros ao contrario


def reverse(a):
	numeros = []
	troca = str(a)
	numeros.append(troca)
	print(numeros[0][::-1])


numero = int(input("Insira um numero: "))
reverse(numero)

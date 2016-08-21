numeros = []
cont = 0

while cont < 5:
	numeros.append(int(input("Insira um número: ")))
	cont += 1

print("O maior numero é: ",max(numeros))

# Criando listas com Impar e par

impar = []
par = []
todos =[]

cont = 0

while cont <= 20:
	num = int(input("Insira um numero: "))
	if num % 2 == 0:
		print("Este numero é PAR!")
		par.append(num)
		todos.append(num)
	else:
		print("Este numero é IMPAR!")
		impar.append(num)
		todos.append(num)
	cont += 1

print("O Vetor dos numeros pares tem os seguintes elementos:\n",impar)
print("já o Vetor dos numeros impares tem os seguintes elementos:\n",par)
print("E o Vetor com todos os conjuntos tem:\n",todos)

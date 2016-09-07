# Calculando a raiz quadrada dos elementos

vetor = []
vetor_mult = []
total = 0

cont = 0

while cont <= 10:
	num = int(input("Insira um numero: "))
	vetor.append(num)
	total += num ** 2
	vetor_mult.append(total)
	cont += 1

print("Os numeros inseridos foram:\n", vetor)
print("E a soma do quadrado dos numeros inseridos é",total)
print("E seu crescimento progressivo foi este\n",vetor_mult)

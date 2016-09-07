# Realizando o calculo dos numeros inteiros

vetor = []
soma = 0
mult = 1

cont = 1

while cont <= 5:
	num = int(input("Insira um numero: "))
	soma += num
	mult *= num
	vetor.append(num)
	cont += 1
print("A soma de todos os valores é:", soma)
print("A multiplicação de todos os valores é:", mult)
print("E todos os numeros inseridos são\n", vetor)

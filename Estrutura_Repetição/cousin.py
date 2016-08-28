# Calculando primos


num = int(input("Insira um numero: "))

if num % 2 == 0 or num % 3 == 0 or num % 4 == 0:
	print("O Numero não é primo")
else:
	print("O numero é primo")

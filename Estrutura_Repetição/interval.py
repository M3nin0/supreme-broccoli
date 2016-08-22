# Peça numeros e some o intervalo entre estes

num1 = int(input("Insira um numero: "))
num2 = int(input("Insira mais um numero: "))
total = 0

if num1 > num2:
	troca = num1
	while troca > num2 + 1:
		troca -= 1
		total += troca
		print(total)

else:
	troca = num2
	while troca > num1 + 1: 
		troca -= 1
		total += troca
		print(total)

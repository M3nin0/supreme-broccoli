par = 0
impar = 0

for i in range(10):
	num = int(input("Insira um numero: "))
	if num % 2 == 0:
		print("Numero par!")
		par += 1
	else:
		print("Numero impar!")
		impar += 1

print("Fora inseridos %d numeros pares e %d impares" %(par, impar))

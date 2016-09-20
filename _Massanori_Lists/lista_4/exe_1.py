# Exe 1 - Numeros aleatorios

from random import randint

nums = []

c = 0
maior = 0
menor = 100

while c <= 10:
	
	num = randint(1,100)
	nums.append(num)

	if num > maior:
		maior = num
	if num < menor:
		menor = num

	c += 1

print("O maior numero é",maior,"e o menor é",menor)

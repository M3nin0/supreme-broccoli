# Numeros pares e impares

import random

nums = []
imp = []
par = []

c = 0

while c <= 20:
	num = random.randint(1,100)
	nums.append(num)
	
	if num % 2 == 0:
		par.append(num)
	else:
		imp.append(num)
	c += 1

print("Os numeros pares são",par,"\nOs impares",imp,"\nE todos os sorteados",nums)

# Exe 3

import random

v1 = []
v2 = []
vI = []

c = 0

while c <= 9:
	num = random.randint(1,100)
	v1.append(num)
	vI.append(num)
	num = random.randint(1,100)
	v2.append(num)
	vI.append(num)
	c += 1

print("A lista 1 tem os elementos",v1)
print("A lista 2 tem os elementos",v2)
print("E a lista que carrega todos os elementos é",vI)

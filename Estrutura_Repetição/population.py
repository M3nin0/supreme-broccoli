c = 0

pA = 80000
pB = 200000

cA = pA * (3 / 100)
cB = pA * (1.5 / 100)

while pA <= pB:
	c += 1
	pA += cA
	pB += cB

print("Serão necessários %d anos para a população A, alcançar a população B" %c)

# A população de um pais

#Cont

cont = 0

# Pais A
pA = 80000
cA = 80000 * 3.0 / 100
tA = pA + cA

# Pais B
pB = 200000
cB = 200000 * 1.5 / 100
tB = pB + cB


while tA < tB:
	tA += tA
	tB += tB
	cont += 1

print ("Serão necessarios %d anos, para que a cidade A alcance a B em numero de habitantes" %cont)

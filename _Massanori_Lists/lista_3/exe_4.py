# Fibonacci

maxi = int(input("Insira até que numero deve ser calculado a sequencia de Fibonacci: "))

a = 0
b = 1
c = 0

while c < maxi:
	c = a + b
	print(c)
	a = b 
	b = c

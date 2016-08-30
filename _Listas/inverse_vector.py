# Lendo alguns vetores e invertendo sua ordem

v = []
c = 0

while c < 10:
	num = int(input("Insira um valor: "))
	v.append(num)
	c += 1

print("Os numeros digitados escritos de maneira inversão são:\n", v[::-1]) 

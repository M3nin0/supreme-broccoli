# Mostrando um vetor com 5 itens

nums = []

c = 0

while c < 5:
	num = int(input("Insira um numero: "))
	nums.append(num)
	c += 1

print("Os numeros digitados foram:\n", nums) 

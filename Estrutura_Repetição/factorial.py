# Calculando o valor fatorial

num = int(input("Insira um numero: "))

c = num

for i in range(c - 1):
	c -= 1
	num *= c
	if c <= 0:
		print(num)
print("O fatorial é",num)

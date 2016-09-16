# Definindo se o valor é positivo ou negativo

def ver(a):
	if a >= 0:
		print("Positivo")
	if a < 0:
		print("Negativo")

num = int(input("Insira um numero: "))

ver(num)
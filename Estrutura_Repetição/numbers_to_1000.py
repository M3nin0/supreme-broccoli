# O Maior e o menor numero

lista = []

while 1:
	num = int(input("Insira um numero, ou precione 0 para sair: "))
	if num >= 0 and num <= 1000:
		if num == 0:
			print("O Maior numero é: %d\nO Menor:%d\nE a soma entre esses é %d" %(max(lista), min(lista),max(lista) + min(lista)))
			break
		lista.append(num)
	else:
		print("Os numeros devem ser entre 0 e 1000:")
		break


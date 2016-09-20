# O Teorema de euclides

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

divs = []

if num1 and num2 % 2 != 0:
	print("O MDC é 1")

if num1 > num2 or num2 > num1:
	if num1 % num2 == 0 and num1 / num2 == 2:
		print("O MDC é",num2)
	else:
		while 1:
			div = num1 % num2
			num1 = num2
			num2 = div
			divs.append(div)
			if num1 % num2 == 0:
				print("O MDC é",min(divs))
				break

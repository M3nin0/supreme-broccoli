# Calculando excedente

peso = int(input("Insira o peso total dos peixes: "))


if peso > 50:
	a = peso - 50
	m = a * 4
	print ("Você exedeu",a,"Kg, e sua multa é R$",m)
else:
	print("Você esta dentro dos limites permitidos")


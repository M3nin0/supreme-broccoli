# Verificando os três lados de um triangulo e definindo seu tipo

l1 = int(input("Insira o valor do lado L1 do triangulo: "))
l2 = int(input("Insira o valor do lado L2 do triangulo: "))
l3 = int(input("Insira o valor do lado L3 do triangulo: "))

if l1 == l2 and l1 == l3:
	print ("Este triangulo é Equilatero")

if l1 != l2 and l1 != l3:
	print ("Este triangulo é Escaleno")

if l1 == l2 and l1 != l3 or l1 != l2 and l1 == l3:
	print ("Este triangulo é Isósceles")

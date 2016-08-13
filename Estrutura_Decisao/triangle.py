L1 = int(input("Insira o lado A do triangulo:" ))
L2 = int(input("Insira o lado B do triangulo: "))
L3 = int(input("Insira o lado C do trinagulo: "))

if L1 == L2 and L1 == L3:
	print("O triangulo é: Equilatero")

elif L1 == L2 or L1 == L3:
	print("O triangulo é: Isósceles ")

elif L1 != L2 or L3:
	print("O triangulo é: Escaleno")

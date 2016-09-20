# Exe 3 - Numeros pares


inicio = 1067
fim = 3627
pares_7 = 0

while inicio <= fim:
	if inicio % 2 == 0 and inicio % 7 == 0:
		pares_7 += 1

	inicio += 1

print("%d que são pares e divisiveis por 7" %pares_7)

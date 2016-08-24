# Realizar a potenciação sem o uso da função de elevação =D
base = int(input("Insira a base do calculo de potenciação: "))
expoente = int(input("Insira a numero do expoente que ira elevar a base: "))

c = base

for vezes in range(expoente - 1):
	base *= c 
		
print(base)

# Armazenando informações de pessoas

idade = []
altura = []

ct = 0

while ct <= 5:
	idadE = int(input("Insira sua idade: "))
	idade.append(idadE)
	alturA = float(input("Insira sua altura: "))
	altura.append(alturA)
	ct += 1

print("Os valores de idades inseridos em ordem inversão são:\n",idade[::-1])
print("Já os valores de altura inseridos em ordem inversa são:\n",altura[::-1])

# Gerando um vetor intermediario com elemento de dois outros vetores

vetorUM = []
vetorMED = []
vetorDOIS = []

ct = 1

while ct <= 10:
	
	elm = int(input("Insira um valor do vetor 1: "))
	vetorUM.append(elm)
	vetorMED.append(elm)
	
	elm = int(input("Insira um valor do vetor 2: "))
	vetorDOIS.append(elm)
	vetorMED.append(elm)

	ct += 1

print("Os elementos inseridos no primeiro vetor são:\n", vetorUM)
print("Os elementos inseridos no segundo vetor são:\n", vetorDOIS)
print("E o vetor gerado com o elementos dos dois vetores tem os seguintes elementos:\n", vetorMED)

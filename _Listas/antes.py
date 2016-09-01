# Calculando as consoantes

vetor = []
c = 0
i = 0
while c <= 10:
	letra = input("Insira uma letra: ")
	if letra not in "aeiou":
		i += 1
		vetor.append(letra)
	c += 1

print("Foram lidas %s consoantes\nE são elas: %s" %(i,vetor))	

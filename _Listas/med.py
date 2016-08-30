# Calculando a nota e as medias

notas = []
c = 0

while c < 4:
	nota = int(input("Insira uma nota: "))
	notas.append(nota)
	c += 1

print("As notas obtidas foram",notas,", e a média é", (sum(notas)/4))

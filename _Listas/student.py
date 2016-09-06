# Calculando a media dos alunos utilizando vetores

media_maior = []
medias_total = []

cont = 0

while cont <= 10:
	nota1 = int(input("Insira a sua primeira nota: "))
	nota2 = int(input("Insira a sua segunda nota: "))
	nota3 = int(input("Insira sua terceira nota: "))
	nota4 = int(input("Insira sua quarta nota: "))
	media = (nota1 + nota2 + nota3 + nota4) / 4
	if media >= 7:
		media_maior.append(media)
		medias_total.append(media)
	else:
		medias_total.append(media)
	cont += 1

print("As melhores medias foram\n", media_maior)
print("E abaixo temos todas as medias\n", medias_total)

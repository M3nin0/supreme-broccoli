# Prova de saltos

nome = input("Insira o nome do atleta: ")

saltos = []
salt = 0
cont = 1 

while cont <= 5:
	pulo = float(input("Insira o valor do salto: "))
	saltos.append(pulo)
	salt += pulo
	cont += 1

print("Resultado Final")
print("Atleta: ", nome)
print("Saltos: ", saltos)
print("Média dos saltos:",(salt / 5))

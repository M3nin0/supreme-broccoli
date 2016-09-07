# Quem é o culpado

perguntas = []

ct = 0
pt = 0

quest = input("Você telefonou a vitima: ")
perguntas.append(quest)
quest = input("Vocẽ esteve no local do crime: ")
perguntas.append(quest)
quest = input("Você mora perto da vitima? ")
perguntas.append(quest)
quest = input("Devia para a vitima? ")
perguntas.append(quest)
quest = input("Já trabalhou com a vitima? ")
perguntas.append(quest)

while ct <= len(perguntas) - 1:
	if perguntas[ct] in "sim":
		pt += 1
	ct += 1

if pt >= 1 and pt <= 2:
	print("Você é um suspeito")

elif pt >= 3 and pt <= 4:
	print("Você é cumplice!")

if pt == 5:
	print("CULPADO,CULPADO, VOCÊ SERÁ PRESO!!!")

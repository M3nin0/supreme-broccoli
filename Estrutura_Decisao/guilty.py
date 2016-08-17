print("Serão feitas algumas perguntas para você sobre o crime que ocorreu\nResponda apenas com 'Sim' ou 'Não'")
pA = input("Você telefonou para a vitima?\n: ")
pB = input("Esteve no local do crime?\n: ")
pC = input("Mora perto da vitima?\n: ")
pD = input("Devia para a vitima?\n: ")
pE = input("Já trabalhou com a vitima\n: ")

clas = 0

if pA == "Sim":
	clas += 1
if pB == "Sim":
	clas += 1
if pC == "Sim":
	clas += 1
if pD == "Sim":
	clas += 1
if pE == "Sim":
	clas += 1

if clas == 2:
	print ("Você é um suspeito, tenha CUIDADO!")

elif clas <= 4:
	print ("Você é cumplice, esta PRESA!")

elif clas == 5:
	print ("CULPADO, VOCẼ ESTA PRESO (A)") 

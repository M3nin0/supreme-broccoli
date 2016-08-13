nota1 = float(input("Insira uma nota que obteve durante o semestre: "))
nota2 = float(input("Insira mais uma nota que obteve este semestre: "))

nota = (nota1 + nota2) / 2 

if nota >= 9 and nota == 10:
	print ("Aprovado com A")
elif nota >= 7.5 and nota < 9:
	print ("Aprovado com B")
elif nota >= 6 and nota < 7.5:
	print ("Aprovado com C")
elif nota >= 4 and nota < 6:
	print ("Aprovado com D")
elif nota < 4:
	print ("REPROVADO =(")	

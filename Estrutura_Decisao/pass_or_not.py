nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terçeira nota: "))
nota_4 = float(input("Insira a quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media == 10:
    print ("Aprovado com Distinção")
elif media >= 7:
    print ("Aprovado!")
elif media < 7:
    print ("Reprovado!")

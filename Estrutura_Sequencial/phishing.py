peso = float(input("Quantos quilos de peixe você pescou?: "))
multa = (peso - 50) * 4

if peso > 50:
    print ("Você terá de pagar uma multa de:",multa)
else:
    multa = 0
    print ("Seu imposto é",multa)

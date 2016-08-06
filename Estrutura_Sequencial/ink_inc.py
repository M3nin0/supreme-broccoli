area = float(input("Insira o tamanho da area a ser pintada: "))
if int(area / 3) == 0:
    print ("Você devera comprar",int(area + 1) / 3)
print ("E esta quantia de latas custa",int(area / 3 * 80))

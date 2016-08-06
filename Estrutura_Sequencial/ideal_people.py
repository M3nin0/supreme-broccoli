peso = float(input("Insira sua altura: "))
sexo = input("Você é homem ou mulher?\n")

if sexo == "homem":
    print ("Seu peso ideal é:",(72.7 * peso) - 58)
else:
    print ("Seu peso idel é:", (62.1 * peso) - 44.7)

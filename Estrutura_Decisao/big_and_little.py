num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 > num2 and num1 > num3:
    print ("O Número %d é o maior" %num1)
elif num1 < num2 and num1 < num3:
    print ("O número %d é o menor" %num1)

if num2 > num1 and num2 > num3:
    print ("O Número %d é o maior" %num2)
elif num2 < num1 and num2 < num3:
    print ("O número %d é o menor" %num2)

if num3 > num1 and num3 > num2:
    print ("O Número %d é o maior" %num3)
elif num3 < num1 and num3 < num2:
    print ("O número %d é o menor" %num3)

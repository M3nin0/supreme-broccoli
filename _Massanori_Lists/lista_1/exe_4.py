# Calculando aumento do salario

salario = int(input("Insira seu salario: "))
aumento = int(input("Insira qual será a procentagem do aumento de seu salario: "))

ganho = salario * (aumento / 100)

print ("Seu aumento é de",ganho,"\nSeu salario passa a ser",ganho + salario)


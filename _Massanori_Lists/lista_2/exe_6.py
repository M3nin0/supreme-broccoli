horas = float(input("Quantas horas você trabalha por mes?\n"))
valor = float(input("E quanto vale sua hora?\n"))


salario = horas * valor

ir = (salario / 100) * 11
inss = (salario / 100) * 8
sindicato = (salario / 100) * 5
sb = salario - (ir + inss + sindicato)

print ("Seu salario é de %.2f\nPagou de INSS %.2f\nSindicato: %.2f\nImposto de renda %.2f\nSeu salario Bruto é: %.2f" %(salario,inss,sindicato,ir,sb))


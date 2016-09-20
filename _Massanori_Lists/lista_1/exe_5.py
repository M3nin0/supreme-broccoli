# Preço da mercadoria e seu desconto

mercad = int(input("Insira o valor de seu produto: "))
porcent = int(input("Insira a porcentagem de desconto que você receberá: "))
desc = mercad * (porcent / 100)
print ("O valor do desconto é:",desc)
print ("E você irá pagar:",mercad - desc)

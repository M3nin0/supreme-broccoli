prod1 = float(input("Insira o valor do produto A: "))
prod2 = float(input("Insira o valor do produto B: "))
prod3 = float(input("Insira o valor do produto C: "))

if prod1 < prod2 and prod1 < prod3:
    print ("Escolha o produto A é o mais barato")
elif prod2 < prod1 and prod2 < prod3:
    print ("Escolha o produto B é o mais barato")
elif prod3 < prod1 and prod3 < prod2:
    print ("Escolha o produto C é o mais barato")

prod1 = float(input("Insira o valor do produto A: "))
prod2 = float(input("Insira o valor do produto B: "))
prod3 = float(input("Insira o valor do produto C: "))

if prod1 > prod2 and prod2 > prod3:
	print(prod3,prod2,prod1)

elif prod1 > prod3 and prod3 > prod2:
	print(prod2,prod3,prod1)

elif prod2 > prod1 and prod1 > prod3:
	print(prod3,prod1,prod2)

elif prod2 > prod3 and prod3 > prod1:
	print(prod1,prod3,prod2)

elif prod3 > prod2 and prod2 > prod1:
	print(prod1,prod2,prod3)

elif prod3 > prod1 and prod1 > prod2:
	print(prod2,prod1,prod3)

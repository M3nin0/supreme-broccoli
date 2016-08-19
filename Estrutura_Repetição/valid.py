nome = input("Insira seu nome: ")

while len(nome) < 3:
	print("O nome é muito pequeno, insira-o novamente: ")
	nome = input("Insira seu nome: ")

idade = int(input("Insira sua idade: "))

while idade < 0 or idade > 150:
	idade = int(input("Insira sua idade novamente: "))

salario = int(input("Insira seu salario: "))

while salario <= 0:
	salario = int(input("Insira novamente seu salario: "))

sexo = input("Insira seu sexo: ")

while sexo not in 'fm':
	sexo = input("Insira seu sexo novamente: ")

es = input("Insira seu estado civil, utilizando\nS - Solteiro\nC - Casado\nV - Viuvo (a)\nD - Divorciado\n: ")

while es not in "SCVD":
	es = input("Insira seu estado civil novamente: ")

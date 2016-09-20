# Lendo nome de usuario e senha

nome = input("Insira seu nome de usuario: ")
senha = input("Insira sua senha: ")


while nome == senha:
	senha = input("A senha não pode ser igual ao nome. Insira novamente!\n:")


print ("Cadastro realizado com sucesso!!")

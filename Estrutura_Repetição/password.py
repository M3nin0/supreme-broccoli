nome = input('Insira seu nome: ')
senha = input('Insira sua senha: ')

while nome == senha:
	print('A senha não pode ser igual ao seu nome, tente novamente')
	senha = input('Insira sua senha: ')

print('Cadastro feito com sucesso!')

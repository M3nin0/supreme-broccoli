nota = int(input('Insira uma nota entre 0 e 10: '))

while nota < 0 or nota > 10:
	print('Nota invalida!!!')
	nota = int(input('Insira uma nota valida, entre 0 e 10: '))

print('Nota adicionada com sucesso!')

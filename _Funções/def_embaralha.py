def embaralha(palavra):
	c = 0
	troca = ''
	while c < len(palavra):
		troca += palavra[c-1]
		c += 1
	print(troca)

palavra = input("Insira uma palavra para ser embaralhada: ")
embaralha(palavra)
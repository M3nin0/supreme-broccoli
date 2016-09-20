# Numeros que não contem o digito 7

inicio = 18644
fim = 33087

contador = 0

while inicio <= fim:
	if str(2) in str(inicio) and str(7) not in str(inicio):
		contador += 1
	inicio += 1
print(contador)

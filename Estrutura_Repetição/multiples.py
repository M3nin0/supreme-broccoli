# Com ajuda do professor Massa, mas utilizei o For =D
tabuada = 1
for tabuada in range(11):
	n = 1
	print ("Tabuada %d" %tabuada)
	while n <= 10:
		conta = tabuada * n
		print("%d x %d = %d" %(tabuada, n, conta))
		n += 1
	tabuada += 1

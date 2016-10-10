# Fatorial com recursão =D

def fatt(num):
	if num == 0:
		print(1)
	else:
		return num * fatt(num - 1)

fatt(5)

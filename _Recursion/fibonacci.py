# Fibonacci com recursão =D
# Quer aprender tambem ? Acesse https://technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/
# Este conteudo eu vi lá =D

def fibo(num):
	if num == 1 or num == 2:
		return 1
	else:
		# return fibo(7 - 1 = 6) + fibo(7 - 2 = 5)
		return fibo(num - 1) + fibo(num - 2)

print(fibo(7))

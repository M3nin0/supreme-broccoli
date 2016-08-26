c = 1
A = []
while c <= 10:
	num = int(input("Insira o elemento para seu conjunto: "))
	A.append(num)
	c += 1

print("O maior valor digitado foi %d e o menor %d" %(max(A), min(A)))


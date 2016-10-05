string = input("Insira uma palavra: ")

c = 0

while 1:

	print(string[c:])
	c = c + 1
	
	if c > len(string):
		break
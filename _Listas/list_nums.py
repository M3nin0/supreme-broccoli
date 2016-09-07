# Verificando todos os elementos de uma lista e suas caracteristicas

numeros = []
a_media = []

c = 1
maior = 0

while 1:
	num = int(input("Insira um numero: "))
	if num == -1:
		break
	numeros.append(num)

media =  sum(numeros) / len(numeros)

while 1:
	if numeros[c] > media:
		maior += 1
		a_media.append(numeros[c])
	if c == len(numeros) - 1:
		break
	c += 1


print("Foram lidos", len(numeros))
print("Os valores lidos são\n", numeros)
print("Estes na ordem inversa são\n", numeros[::-1])
print("A soma de todos os valores é", sum(numeros))
print("A media destes é:", media)
print("Existem %d numeros que tem valor acima da media" %maior)
print("São eles:\n", a_media)
print("\n'Nunca acredite no contador de histórias, apenas na história'")

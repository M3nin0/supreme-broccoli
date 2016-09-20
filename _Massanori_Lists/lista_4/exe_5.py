# Exe 5

c = 0

texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

texto = str.replace(texto, ".","")
texto = str.replace(texto, ":","")
texto = str.replace(texto, ",","")

lista = texto.lower().split()

python = []

while 1:
        if c == len(lista):
                break
        if lista[c][0] in "python" and len(lista[c]) > 4 or lista[c][-1] in "python" and len(lista[c]) > 4:
                python.append(lista[c])
        c += 1

print("Este texto possui %d palavras que tem mais letras que 4 caracteres e começam ou terminam com as letras de 'python'"%(len(python)))
print("E são elas:\n", python)


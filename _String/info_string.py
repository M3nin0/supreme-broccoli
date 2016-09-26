# Definindo as caracteristicas da string

string_1 = input("Insira a primeira frase: ")
string_2 = input("Insira a segunda frase: ")

print("O texto 1 tem",len(string_1),"letras")
print("O texto 2 tem",len(string_2),"letras")

if string_1 == string_2:
	print("Os textos são iguais =D")
else:
	print("Os textos são diferentes =(")
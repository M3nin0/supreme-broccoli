# Calculando o valor do carro

km = float(input("Insira quantos quilometros o carro já rodou: "))
dias = int(input("Insira a quantidade de dias que o carro ficou alugado: "))

preço = (dias * 60) + (km * 0.15)

print ("Você gastou no total com o carro, isto contando aluguel + Quilômetragem é:\n",preço,"R$")

# Calcule Dias, horas, minutos e segundos, e transforme-o em segundos
dias = int(input("Insira o numero de dias: "))
horas = int(input("Insira as horas: "))
minutos = int(input("Insira os minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

total = (dias * 24 * 60 * 60 )  + (horas * 60 * 60 ) + ( minutos * 60 * 60 ) + segundos
print ("Todo esse tempo em minutos é igual %i:" %(total))

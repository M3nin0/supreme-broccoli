# Calculando o tempo de vida perdido por um fumante

cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Quantos anos você fumou? "))

total = (anos * 365) * cigarros

print ("Você fumou em todo este tempo",total," cigarros, e isto lhe custou",total * 10 / 1440,"dias de vida")

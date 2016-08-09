num_1 = int(input("Insira um numero: "))
num_2 = int(input("Insira um segundo numero: "))
num_3 = int(input("Insira mais um numero: "))

if num_1 > num_2 and num_3:
    print ("O", num_1, "é o maior número")
elif num_2 > num_1 and num_3:
    print ("O", num_2, "é o maior número")
elif num_3 > num_1 and num_2:
    print ("O", num_3, "é o maior número")

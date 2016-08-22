cont = 0
nums = 0

while cont < 5:
	num = int(input("Insira um numero: "))
	nums += num
	cont += 1

print("A soma dos numeros é %d e a media é %d" %(nums, nums / 5))

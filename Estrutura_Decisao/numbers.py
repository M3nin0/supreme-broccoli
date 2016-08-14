num = str(input("Insira um valor entre 0 a 1000: "))

if len(str(num)) == 1:
	if int(num) > 1:
		print ("%s Unidades" %num)
	else:
		print ("%s Unidade" %num)

if len(str(num)) == 2:
	d = num[:1]
	u = num[1:2]
	if int(d) > 1 and int(u) > 1:
		print("São %s dezenas e %s unidades" %(d,u))
	elif int(d) > 1 and int(u) == 1:
		print("São %s dezenas e %s unidade" %(d,u))
	elif int(d) == 1 and int(u) > 1:
		print("São %s dezena e %s unidades" %(d,u))

if len(str(num)) == 3:
	c = num[:1]
	d = num[1:2]
	u = num[2:3]
	if int(c) > 1 and int(d) > 1 and int(u) > 1:
		print("São %s centenas, %s dezenas e %s unidades" %(c,d,u))
	elif int(c) == 1 and int(d) > 1 and int(u) > 1:
		print("São %s centena, %s dezenas e %s unidades" %(c,d,u))
	elif int(c) > 1 and int(d) == 1 and int(u) > 1:
		print("São %s centenas, %s dezena e %s unidades" %(c,d,u))
	elif int(c) > 1 and int(d) > 1 and int(u) == 1:
		print("São %s centena, %s dezenas e %s unidade" %(c,d,u))

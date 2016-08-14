date = input("Insira a data com formato --> (dd/mm/aaaa)\n:")

dias = ["01","02","03","04","05","06","07","08","09",
	"10","11","12","13","14","15","16","17","18",
	"19","20","21","22","23","24","25","26","27",
	"28","29","30","31"]

meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]


dd,mm,aaaa = date.split("/")

if dd not in dias:
	print("Campo Dia Incorreto!")

elif mm not in meses:
	print("Campo Meses Incorreto!")

else:
	print("Sua data foi inserida corretamente")

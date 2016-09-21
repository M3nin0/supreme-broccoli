def meses(data):
	meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto', 'Setembro','Outubro', 'Novembro', "Dezembro"]
	dd,mm,aaaa = data.split('/')
	print (meses[int(mm) - 1])


data = input("Insira uma data, da seguinte maneira: [DD/MM/AAAA]")
meses(data)
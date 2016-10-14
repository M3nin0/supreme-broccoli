#Dispertador simples
#Install MPG123 for play Song

from datetime import datetime
import subprocess
import sys

acorda = sys.argv

while 1:
	atual = datetime.now()
	troca = str(atual.hour) + ":" + str(atual.minute)
	if troca == str(acorda[1]):
		subprocess.run(["clear"])
		print('''
			  ___  _____ _________________  ___  
			 / _ \/  __ \  _  | ___ \  _  \/ _ \ 
			/ /_\ \ /  \/ | | | |_/ / | | / /_\ \
			
			| | | | \__/\ \_/ / |\ \| |/ /| | | |
			\_| |_/\____/\___/\_| \_|___/ \_| |_/
 			''')
		subprocess.run(["mpg123","street_fighter_2_guiles_theme-1.mp3"])
		break

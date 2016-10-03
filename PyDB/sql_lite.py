# Código feito com a ajuda do Wiki Python =D
import sqlite3
conect = sqlite3.connect('sqllite.db')

co = conect.cursor()

co.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

co.execute("INSERT INTO stocks VALUES ('2006-01-05','Love Pyton','S2',99,25.15)")


conect.commit()

conect.close()
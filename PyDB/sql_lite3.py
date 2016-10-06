#http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
# Estou aprendendo sobre SQL, quero agradecer o Regis pelo exelente tutorial +D

import sqlite3

conn = sqlite3.connect('teste.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
""")

print('Sucesso =D')

conn.close()

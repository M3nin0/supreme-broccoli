# Importando tkinter e chamando ele de tk
import tkinter as tk

# Definindo a variavel e atribuindo a ela uma nova instancia para ela
janela = tk.Tk()

janela.title("Janela principal")

janela['bg'] = 'green'

# LarguraxAltura+E=T
janela.geometry("300x300+100+100")

# Referencia a variavel acima, com um 'loop infinito'
janela.mainloop()

import tkinter as tk
from tkinter import messagebox

class Tela(tk.Entry): # Um campo de texto para o usuário digitar algo
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="ridge", font=("Arial", 18), justify="right")
        self.grid(row=0, column=0, columnspan=4) # columnspan: permite que um widget ocupe várias colunas.
        self.text = ""
        
        def define_texto(self, texto):
            self.texto = texto
            self.deleta(0, tk.END)
            self.insere(0, texto)

    def obter_texto(self):
        return self.get()
        
class Botao(tk.Botao):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, font=("Arial", 14))

        

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        self.tela = Tela(self)
        self.ultimo_resultado = None
        self.criar_widget()


    def criar_widgets(self):
        botao = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), #('aparece no botao', n° da linha, n° da coluna)
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]


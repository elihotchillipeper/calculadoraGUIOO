import tkinter as tk
from tkinter import messagebox

class Tela(tk.Entry): # Um campo de text para o usuário digitar algo
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="ridge", font=("Arial", 18), justify="right")
        self.grid(row=0, column=0, columnspan=4) # columnspan: permite que um widget ocupe várias colunas.
        self.text = ""
        
        def define_text(self, text):
            self.text = text
            self.deleta(0, tk.END)
            self.insere(0, text)

    def obter_text(self):
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

        for (text, row, col, colspan) in botao:
            if text == '=':
                bta = Botao(self, text, command=self.calculate)
            elif text == 'C':
                bta = Botao(self, text, command=self.clear)
            else:
                bta = Botao(self, text, command=lambda t=text: self.clicar_botao(t))
            bta.grid(row=row, column=col, columnspan=colspan)
            
        self.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            
    def clicar_botao(self, char):
        current_text = self.tela.get_text()
        if char.isdigit() or char == '.':
            self.tela.set_text(current_text + char)
        elif char in '+-*/':
            if current_text and current_text[-1] not in '+-*/':
                self.tela.set_text(current_text + char)
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()        

def calcular(self):
        try:
            expression = self.tela.get_text()
            result = eval(expression)
            self.tela.set_text(str(result))
            self.last_result = result
        except ZeroDivisionError:
            messagebox.showerror("Divisão por zero não é permitida.")
            self.tela.set_text("")
        except Exception as e:
            messagebox.showerror("Erro", f"Operação inválida: {e}")
            self.tela.set_text("")

def clear(self):
        self.tela.set_text("")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
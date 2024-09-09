import tkinter as tk
from tkinter import messagebox

class Tela(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="ridge", font=("Arial", 18), justify="right")
        self.grid(row=0, column=0, columnspan=4)

    def define_text(self, text):
        self.delete(0, tk.END)
        self.insert(0, text)

    def obter_text(self):
        return self.get()

class Botao(tk.Button):
    def __init__(self, parent, text, command=None):
        super().__init__(parent, text=text, font=("Arial", 14), command=command)

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        self.tela = Tela(self)
        self.ultimo_resultado = None
        self.criar_widgets()

    def criar_widgets(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col, colspan) in botoes:
            if text == '=':
                bta = Botao(self, text, command=self.calcular)
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
        current_text = self.tela.obter_text()
        if char.isdigit() or char == '.':
            self.tela.define_text(current_text + char)
        elif char in '+-*/':
            if current_text and current_text[-1] not in '+-*/':
                self.tela.define_text(current_text + char)
        elif char == '=':
            self.calcular()
        elif char == 'C':
            self.clear()

    def calcular(self):
        try:
            expression = self.tela.obter_text()
            result = eval(expression)
            self.tela.define_text(str(result))
            self.ultimo_resultado = result
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            self.tela.define_text("")
        except Exception as e:
            messagebox.showerror("Erro", f"Operação inválida: {e}")
            self.tela.define_text("")

    def clear(self):
        self.tela.define_text("")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()

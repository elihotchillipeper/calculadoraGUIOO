# calculadoraGUIOO]

import tkinter as tk
from tkinter import messagebox

class Display(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="ridge", font=("Arial", 18), justify="right")
        self.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.text = ""

    def set_text(self, text):
        self.text = text
        self.delete(0, tk.END)
        self.insert(0, text)

    def get_text(self):
        return self.get()

class Button(tk.Button):
    def __init__(self, parent, text, command=None):
        super().__init__(parent, text=text, font=("Arial", 14), command=command)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        self.display = Display(self)
        self.last_result = None
        self.create_widgets()

    def create_widgets(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)
        ]

        for (text, row, col, colspan) in buttons:
            if text == '=':
                btn = Button(self, text, command=self.calculate)
            elif text == 'C':
                btn = Button(self, text, command=self.clear)
            else:
                btn = Button(self, text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.display.get_text()
        if char.isdigit() or char == '.':
            self.display.set_text(current_text + char)
        elif char in '+-*/':
            if current_text and current_text[-1] not in '+-*/':
                self.display.set_text(current_text + char)
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()

    def calculate(self):
        try:
            expression = self.display.get_text()
            result = eval(expression)
            self.display.set_text(str(result))
            self.last_result = result
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            self.display.set_text("")
        except Exception as e:
            messagebox.showerror("Erro", f"Operação inválida: {e}")
            self.display.set_text("")

    def clear(self):
        self.display.set_text("")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()


    ///////////////////////////////


    import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        self.display = Display(self)
        self.ultimo_resultado = None
        self.criar_widget()


    def criar_widgets(self):
        botao = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3) #('aparece no botao', n° da linha, n° da coluna)
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3)
        ]






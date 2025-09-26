import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Bonita")
        self.geometry("320x420")
        self.resizable(False, False)
        self.configure(bg="#222831")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TButton', font=('Segoe UI', 16), padding=10, background='#393E46', foreground='#EEEEEE')
        style.map('TButton', background=[('active', '#00ADB5')])

        self.display_var = tk.StringVar()
        display = tk.Entry(self, textvariable=self.display_var, font=('Segoe UI', 24), bd=0, bg='#393E46', fg='#00FFF5', justify='right')
        display.pack(fill='x', padx=10, pady=20, ipady=15)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]

        frame = tk.Frame(self, bg='#222831')
        frame.pack()

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = ttk.Button(frame, text=char, command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=r, column=c, sticky='nsew', padx=5, pady=5)
            frame.grid_rowconfigure(r, weight=1)
        for c in range(4):
            frame.grid_columnconfigure(c, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display_var.set('')
        elif char == '=':
            try:
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except Exception:
                self.display_var.set('Erro')
        else:
            self.display_var.set(self.display_var.get() + char)

if __name__ == "__main__":
    Calculator().mainloop()
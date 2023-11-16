import tkinter as tk

def click():
    valor1 = float(cx_texto1.get())
    valor2 = float(cx_texto2.get())
    print(valor1 + valor2)

#JANELA PRINCIPAL
janela = tk.Tk()
janela.geometry("800x600")
janela.configure(background="#0e131c")
frame = tk.Frame(janela)
frame.pack()

#TITULO/TEXTO
texto = tk.Label(frame, text = "calculadora")
texto["fg"] = "#e61010"
texto.pack()

#CAIXA DE TEXTO
cx_texto1 = tk.Entry(frame)
cx_texto1["fg"] = "#2541b0"
cx_texto1.pack()

cx_texto2 = tk.Entry(frame)
cx_texto2["fg"] = "#2541b0"
cx_texto2.pack()

#BOTÃO
butão = tk.Button(frame, text = "calcular", command = click)
butão["fg"] = "#e61010"
butão.pack()

janela.mainloop()

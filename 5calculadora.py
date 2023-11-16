import tkinter as tk

def click():
    valor1 = float(cx_texto1.get())
    valor2 = float(cx_texto2.get())
    somar = valor1 + valor2
    text.config(text=somar, font= "Carlito 18" , fg="#6f0dbf")
def click1():
    valor1 = float(cx_texto1.get())
    valor2 = float(cx_texto2.get())
    subtrair = valor1 - valor2
    text.config(text=subtrair, font= "Carlito 18" , fg="#6f0dbf")
def click2():
    valor1 = float(cx_texto1.get())
    valor2 = float(cx_texto2.get())
    multiplicar = valor1 * valor2
    text.config(text=multiplicar, font= "Carlito 18" , fg="#6f0dbf")
def click3():
    valor1 = float(cx_texto1.get())
    valor2 = float(cx_texto2.get())
    dividir = valor1 / valor2
    text.config(text=dividir, font= "Carlito 18" , fg="#6f0dbf")

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
butão = tk.Button(frame, text = "somar", command = click)
butão["fg"] = "#e61010"
butão.pack()

butão = tk.Button(frame, text = "subtrair", command = click1)
butão["fg"] = "#e61010"
butão.pack()

butão = tk.Button(frame, text = "multiplicar", command = click2)
butão["fg"] = "#e61010"
butão.pack()

butão = tk.Button(frame, text = "dividir", command = click3)
butão["fg"] = "#e61010"
butão.pack()

#RESULTADO NA TELA
text = tk.Label(frame, text="")
text.pack()

janela.mainloop()
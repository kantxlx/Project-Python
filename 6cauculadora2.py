import tkinter


def btn_somar_click():
    valor1 = float( cx_num1.get() )
    valor2 = float(cx_num2.get() )
    resultado = valor1+valor2
    lbl_resultado.config(text=resultado)

def btn_multi_click():
    valor1 = float( cx_num1.get() )
    valor2 = float(cx_num2.get() )
    resultado = valor1*valor2
    lbl_resultado.config(text=resultado)

def btn_sub_click():
    valor1 = float( cx_num1.get() )
    valor2 = float(cx_num2.get() )
    resultado = valor1-valor2
    lbl_resultado.config(text=resultado)

def btn_div_click():
    valor1 = float( cx_num1.get() )
    valor2 = float(cx_num2.get() )
    resultado = valor1/valor2
    lbl_resultado.config(text=resultado)

janela = tkinter.Tk()


frame = tkinter.Frame(janela)
frame.grid(column=0, row=0)


cx_num1 = tkinter.Entry(frame)
cx_num1.grid(column=0, row=0)


cx_num2 = tkinter.Entry(frame)
cx_num2.grid(column=0, row=1)

lbl_resultado = tkinter.Label(frame,text="||||")
lbl_resultado.grid(column=1,row=2)
lbl_resultado["font"] = ("Arial", "20")
lbl_legenda = tkinter.Label(frame,text="Resultado:")
lbl_legenda.grid(column=0,row=2)

btn_somar = tkinter.Button(frame, text="Somar", command=btn_somar_click)
btn_somar.grid(column=1, row=0)

btn_multi = tkinter.Button(frame, text="Multiplicar", command=btn_multi_click)
btn_multi.grid(column=2, row=0)

btn_div = tkinter.Button(frame, text="Dividir", command=btn_div_click)
btn_div.grid(column=1, row=1)

btn_sub = tkinter.Button(frame,text="Subtrair", command=btn_sub_click)
btn_sub.grid(column=2,row=1)



janela.mainloop()
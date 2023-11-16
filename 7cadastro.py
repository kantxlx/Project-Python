import tkinter as tk

nome = []
idade = []
cpf = []

def salvar():
    nome.append(txt_nome.get())
    idade.append(txt_idade.get())
    cpf.append(txt_cpf.get())

def imprimir():
    lc = tk.StringVar(value=nome)
    lbox_nome.config(listvariable=lc)
    lc = tk.StringVar(value=idade)
    lbox_idade.config(listvariable=lc)
    lc = tk.StringVar(value=cpf)
    lbox_cpf.config(listvariable=lc)

janela = tk.Tk()
frame = tk.Frame(janela)
frame.grid(column=0,row=0)

lbl1 = tk.Label(frame, text="NOME: ")
lbl1.grid(column=0,row=0)
lbl2 = tk.Label(frame, text="IDADE: ")
lbl2.grid(column=1,row=0)
lbl3 = tk.Label(frame, text="CPF: ")
lbl3.grid(column=2,row=0)

txt_nome = tk.Entry(frame)
txt_nome.grid(column=0,row=2)
txt_idade = tk.Entry(frame)
txt_idade.grid(column=1,row=1)
txt_cpf = tk.Entry(frame)
txt_cpf.grid(column=2,row=1)

lbox_nome = tk.Listbox(frame)
lbox_nome.grid(column=0,row=2)
lbox_idade = tk.Listbox(frame)
lbox_idade.grid(column=1,row=2)
lbox_cpf = tk.Listbox(frame)
lbox_cpf.grid(column=2,row=2)



botao = tk.Button(frame, text="Imprimir", command=imprimir)
botao.grid(column=0,row=3)
botao = tk.Button(frame, text="Salvar", command=salvar)
botao.grid(column=2,row=3)

janela.mainloop()

import tkinter as tk
from tkinter import messagebox

class EstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EFG Mercado")
        self.root.configure(bg='white')
        self.root.geometry("1000x500")
        self.root.resizable(False, False)

        self.produtos = {}

        self.frame_principal = tk.Frame(root, bg='white')
        self.frame_principal.pack(pady=20)

        self.label_nome = tk.Label(self.frame_principal, text="Nome:", bg='white', fg='green')
        self.label_nome.grid(row=0, column=0, sticky=tk.W)
        self.entry_nome = tk.Entry(self.frame_principal)
        self.entry_nome.grid(row=0, column=1)

        self.label_quantidade = tk.Label(self.frame_principal, text="Quantidade:", bg='white', fg='green')
        self.label_quantidade.grid(row=1, column=0, sticky=tk.W)
        self.entry_quantidade = tk.Entry(self.frame_principal)
        self.entry_quantidade.grid(row=1, column=1)

        self.button_adicionar = tk.Button(self.frame_principal, text="Adicionar ao Estoque", bg='green', fg='white', command=self.adicionar_estoque)
        self.button_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

        self.button_vender = tk.Button(self.frame_principal, text="Vender Produto", bg='green', fg='white', command=self.vender_produto)
        self.button_vender.grid(row=3, column=0, columnspan=2, pady=10)

        self.frame_pesquisa = tk.Frame(root, bg='white')
        self.frame_pesquisa.pack(pady=10)

        self.label_pesquisar = tk.Label(self.frame_pesquisa, text="Pesquisar:", bg='white', fg='green')
        self.label_pesquisar.grid(row=0, column=0, sticky=tk.W)
        self.entry_pesquisar = tk.Entry(self.frame_pesquisa)
        self.entry_pesquisar.grid(row=0, column=1)
        self.entry_pesquisar.bind("<KeyRelease>", self.atualizar_lista)

        self.frame_estoque = tk.Frame(root, bg='white')
        self.frame_estoque.pack()

        self.label_estoque = tk.Label(self.frame_estoque, text="Estoque:", bg='white', fg='green')
        self.label_estoque.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.lista_estoque = tk.Listbox(self.frame_estoque, width=40)
        self.lista_estoque.grid(row=1, column=0, columnspan=2, pady=10)

        self.frame_analise = tk.Frame(root, bg='white')
        self.frame_analise.pack(pady=10)

        self.button_menos_vendidos = tk.Button(self.frame_analise, text="Produtos com menor qtd. em estoque", bg='green', fg='white', command=self.produtos_menos_vendidos)
        self.button_menos_vendidos.grid(row=0, column=0, padx=10)

        self.button_mais_vendidos = tk.Button(self.frame_analise, text="Produtos com maior qtd. em estoque", bg='green', fg='white', command=self.produtos_mais_vendidos)
        self.button_mais_vendidos.grid(row=0, column=1, padx=10)

        self.atualizar_lista()

    def adicionar_estoque(self):
        nome = self.entry_nome.get()
        quantidade = int(self.entry_quantidade.get())

        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade

        messagebox.showinfo("Sucesso", f"{quantidade} unidades de {nome} adicionadas ao estoque.")

        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.atualizar_lista()

    def vender_produto(self):
        nome = self.entry_nome.get()
        quantidade = int(self.entry_quantidade.get())

        if nome in self.produtos and self.produtos[nome] >= quantidade:
            self.produtos[nome] -= quantidade
            messagebox.showinfo("Sucesso", f"{quantidade} unidades de {nome} vendidas.")
        else:
            messagebox.showerror("Erro", "Produto não disponível no estoque ou quantidade insuficiente.")

        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.atualizar_lista()

    def atualizar_lista(self, event=None):
        termo_pesquisa = self.entry_pesquisar.get().lower()
        self.lista_estoque.delete(0, tk.END)

        for produto, quantidade in self.produtos.items():
            if termo_pesquisa in produto.lower():
                self.lista_estoque.insert(tk.END, f"{produto}: {quantidade} unidades")

    def produtos_menos_vendidos(self):
        produtos_ordenados = sorted(self.produtos.items(), key=lambda x: x[1])
        messagebox.showinfo("Produtos Menos Vendidos", f"Os produtos menos vendidos são:\n\n{produtos_ordenados[:5]}")

    def produtos_mais_vendidos(self):
        produtos_ordenados = sorted(self.produtos.items(), key=lambda x: x[1], reverse=True)
        messagebox.showinfo("Produtos Mais Vendidos", f"Os produtos mais vendidos são:\n\n{produtos_ordenados[:5]}")

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    app.iniciar()
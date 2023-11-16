class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f'{quantidade} unidades do produto {self.nome} foram adicionadas ao estoque.')

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f'{quantidade} unidades do produto {self.nome} foram removidas do estoque.')
        else:
            print(f'Não é possível remover {quantidade} unidades do produto {self.nome} do estoque. 'f'A quantidade em estoque é de {self.quantidade} unidades.')

    def calcular_valor_total(self):
        valor_total = self.preco * self.quantidade
        resposta = input("Se deseja ver o valor total em produtos digite '1' se não so aperta qualquer outra tecla: ")
        if resposta == 1:
            print("O valor total de produtos e de:", valor_total)

produtos = []

while True:
    print("1 - Cadastrar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade em estoque: "))

        produto = Produto( nome, preco, quantidade)
        produtos.append(produto)
        print(f'O produto {nome} foi cadastrado com sucesso!')

    elif opcao == "2":
        if len(produtos) == 0:
            print("Não há produtos cadastrados.")
        else:
            nome = input("Digite o nome do produto que deseja remover: ")
            encontrado = False

            for produto in produtos:
                if produto.nome.lower() == nome.lower():
                    produtos.remove(produto)
                    encontrado = True
                    print(f'O produto {produto.nome} foi removido com sucesso!')
                    break

            if not encontrado:
                print(f'O produto {nome} não foi encontrado.')

    elif opcao == "3":
        if len(produtos) == 0:
            print("Não há produtos cadastrados.")
        else:
            print("\nPRODUTOS CADASTRADOS:")
            for produto in produtos:
                print(f'Nome: {produto.nome} | Preço: R${produto.preco:.2f} | Quantidade em estoque: {produto.quantidade}')

    elif opcao == "4":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
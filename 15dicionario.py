pessoas_cadastradas = []

for i in range(0,10):
    nome = input("digite o nome: ")
    cpf = int(input("digite o cpf: "))
    idade = int(input("digite a idade: "))
    telefone = int(input("digite o numero de telefone: "))
    cadastro = {"nome": nome, "cpf": cpf, "idade": idade, "telefone": telefone}
    pessoas_cadastradas.append(cadastro)



for pc in pessoas_cadastradas:
    print(pc["nome"], pc["cpf"], pc["idade"], pc["telefone"])
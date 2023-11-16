class Chinela:
    def __init__(self, cor, modelo, marca):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca


    def apresentar(self):
        print("A cor da minha chinela é: ", self.cor, "o modelo da chinela é: ", self.modelo, "A marca da sua chinela é: ", self.marca)
chinelas = []
while True:
    Chinela01 = Chinela(input("digite a cor da sua chinela: "), input("digite o modelo da sua chinela: "), input("digite a marca da sua chinela: "))
    chinelas.append(Chinela01)
    resposta = int(input("se deseja sair digite '1': "))
    if resposta == 1:
        break

 
for c in chinelas:
    c.apresentar()

class automovel:
    def __init__(self, cor, ano_de_fabricação, modelo):
        self.cor = cor
        self.ano_de_fabricação = ano_de_fabricação
        self.modelo = modelo

class moto(automovel):
    def fazer_barulho_chato(self):
        print("Pode matar o piloto da moto")

class carro(automovel):
    def cavalo_de_pau(self):
        print("esse cara do carro e foda")

moto01 = moto("verde", 2022, "Kawasaki Ninja 650 R")
carro01 = carro("prata", 2012,"Fiat Uno")

moto01.fazer_barulho_chato()
carro01.cavalo_de_pau()
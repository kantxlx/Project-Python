class Veiculo:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combsutivel = 0
        self.status = False
        self.capacete = False

class Carro(Veiculo):
    def ligar(self):
        self.status = True
        print("CARRO LIGADO!")

    def desligar(self):
        self.status = False
        print("CARRO DESLIGADO!")

    def andar(self, valor_andado):
        if self.status == True:
            gasto = valor_andado / self.consumo
            self.combsutivel = self.combsutivel - gasto
        else:
            print("Carro desligado, dê partida no motor!")

    def abastecer(self, valor_abastecido):
        if self.status == False:
            self.combsutivel = self.combsutivel + valor_abastecido
            print(f"{valor_abastecido} litros abastecido com sucesso!")
        else:
            print("Carro está ligado, desligue para abastecer!")
    
    def ver_tanque(self):
        if self.status == True:
            print(f"Seu tanque possui {self.combsutivel} litros")
        else:
            print("Carro desligado, ligue para ver seu tanque!")

class Moto(Veiculo):
    def ligar(self):
        self.status = True
        print(f"MOTO LIGADA!")

    def desligar(self):
        self.status = False
        print(f"MOTO DESLIGADA!")

    def andar(self, valor_andado):
        if self.status == True:
            gasto = valor_andado / self.consumo
            self.combsutivel = self.combsutivel - gasto
        else:
            print("Moto desligada, dê partida no motor!")

    def abastecer(self, valor_abastecido):
        if self.status == False:
            self.combsutivel = self.combsutivel + valor_abastecido
            print(f"{valor_abastecido} litros abastecido com sucesso!")
        else:
            print("Moto ligada, desligue para abastecer!")
    
    def ver_tanque(self):
        if self.status == True:
            print(f"Seu tanque possui {self.combsutivel} litros")
        else:
            print("Moto desligada, ligue para ver seu tanque!")
    
    def por_capa(self):
        self.capacete = True
        print("CAPACETE COLOCADO! ")
    
    def tirar_capa(self):
        self.capacete = False
        print("CAPACETE TIRADO! ")

    def andar(self, valor_andado):
        if self.status == True:
            gasto = valor_andado / self.consumo
            self.combsutivel = self.combsutivel - gasto
        else:
            print("Moto desligada, dê partida no motor!")

print(f"\n 1- MOTO \n 2- CARRO")
escolha_veiculo = int(input(f"Digite o tipo do seu automóvel: "))
if escolha_veiculo == 1:
    moto = Moto(int(input("Digite quantos Km seu automovel faz por litro: ")))
elif escolha_veiculo == 2:
    carro = Carro(int(input("Digite quantos Km seu automovel faz por litro: ")))

while True:
    if escolha_veiculo == 1:
        print(f"\n 1- ABASTECER MOTO \n 2- ANDAR COM MOTO \n 3- VER TANQUE \n 4- LIGAR MOTO \n 5- DESLIGAR MOTO")
        num = int(input())
        if num == 1:
            moto.abastecer(int(input("Digite quantos litros deseja abastecer: ")))
        elif num == 2:
            moto.andar(int(input("Digite quantos km deseja andar: ")))
        elif num == 3:
            moto.ver_tanque()
        elif num == 4:
            moto.ligar()
        elif num == 5:
            moto.desligar()

        resposta = input("Aperte ENTER para confirmar, ou digite NÃO para sair: ").upper()
        if resposta == "NAO" or resposta == "N" or resposta == "NÃO":
            break

    elif escolha_veiculo == 2:
    
        while True:    
            print(f"\n 1- ABASTECER CARRO \n 2- ANDAR COM CARRO \n 3- VER TANQUE \n 4- LIGAR CARRO \n 5- DESLIGAR CARRO")
            num = int(input())
            if num == 1:
                carro.abastecer(int(input("Digite quantos litros deseja abastecer: ")))
            elif num == 2:
                carro.andar(int(input("Digite quantos km deseja andar: ")))
            elif num == 3:
                carro.ver_tanque()
            elif num == 4:
                carro.ligar()
            elif num == 5:
                carro.desligar()

            resposta = input("Aperte ENTER para confirmar, ou digite NÃO para sair: ").upper()
            if resposta == "N" or resposta == "NÃO" or resposta == "NAO":
                break

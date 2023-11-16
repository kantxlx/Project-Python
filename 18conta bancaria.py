class conta_bancaria:
    def __init__(self, nome_do_titular, saldo):
        self.nome_do_titular = nome_do_titular
        self.saldo = saldo

    def apresentar(self):
        print("Titular: ", self.nome_do_titular, "saldo: ", self.saldo)

    def depositar(self):
        deposito = float(input("digite o valor que deseja depositar: "))
        self.saldo = self.saldo + deposito
        print("agora seu saldo e de: ", self.saldo)

    def saque(self):
        saque = float(input("digite o valor que deseja sacar: "))
        self.saldo = self.saldo - saque
        if saque > self.saldo:
            print("saldo insuficiente")
        else:
            print("agora seu saldo e de: ", self.saldo)
    
    def saldo(self):
        print(usuario01.saldo)

usuario01 = conta_bancaria("Diego Afonso", 980.57)
print(usuario01.nome_do_titular)


comando = int(input("O que deseja fazer? para sacar 1, para depositar 2 e para ver o saldo 3: "))

if comando == 1:
    usuario01.saque()
elif comando == 2:
    usuario01.depositar()
elif comando == 3:
    usuario01.saldo()



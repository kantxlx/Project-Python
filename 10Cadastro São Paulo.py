São_Paulo = [""]

while True:
    São_Paulo.append(input("escreva seu nome para entrar no São Paulo: "))
    encerrar = (input("se não que mais inscrever ninguem digite ""sair"": "))
    if encerrar == "sair":
        break

f = open("cadastro São Paulo", "a+")

for cadatro in São_Paulo:
    f.write(cadatro)
    f.write("\n")

f.close()
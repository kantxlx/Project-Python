estados = int(input())
eu = []

for i in range(estados):
    estado, alcool, gasolina = input().split()
    alcool, gasolina = float(alcool), float(gasolina)


    valor = alcool / gasolina

    if valor <= 0.7:
        print(estado)
    
if valor > 0.7:
    eu.append(valor)

if len(eu) == estados:
    print("*")


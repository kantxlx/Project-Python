n = int(input())
tamanhos = input().split()
p = int(input())
m = int(input())

p_produzidos = tamanhos.count("1")
m_produzidos = tamanhos.count("2")

if  p_produzidos >= p and m_produzidos >= m:
    print("S")
else:
    print("N")
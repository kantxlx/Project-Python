def fe_para_celsius(c):
    return (c * 1.8) +32
def celsius_para_fe(f):
    return (f - 32) /1.8

celsius = fe_para_celsius(int(input("digite os graus celsius: ")))
farenheit = celsius_para_fe(int(input("digite os graus em farenheit: ")))

print(celsius)
print(farenheit)


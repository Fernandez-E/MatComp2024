linhas, x, fx, dx2 = [], [], [], []

with open('derivacao.txt', 'r') as dados:
    for linha in dados:
        x.append(float(linha[0:2]))
        fx.append(float(linha[3:-1]))

dx = x[0] - x[1]
i=1
while i < 10:
    derivada = (fx[i+1] - 2*fx[i] + fx[i-1]) / (dx ** 2)
    dx2.append(derivada)
    i+=1

print(dx2)
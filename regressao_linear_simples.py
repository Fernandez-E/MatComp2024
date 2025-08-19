x, y = [], []
temp = 0

soma_x, soma_y, soma_xy, soma_x2 = 0, 0, 0, 0
sxx, sxy = 0, 0

ve, vt = 0, 0

print('Insira os valores para a regressao. Para parar de inserir, digite o valor -9999')

while temp != -9999:
    temp = float(input('Insira um valor para x: '))
    if temp == -9999:
        break
    x.append(temp)
    temp = float(input('Insira um valor para y: '))
    if temp == -9999:
        x.pop()
        break
    y.append(temp)
    print(f'Valores x: {x}')
    print(f'Valores y: {y}')

n = len(x)

# calculo de somatorio utilizando metodo interno de listas:

soma_x = sum(x)

# calculo de somatorio utilizando laços de repetição:
# usando while
i = 0
while i < len(x):
    soma_x2 += x[i] ** 2
    soma_xy += x[i] * y[i]
    i += 1

# usando for
for i in range(len(x)):
    soma_y += y[i]

sxx = soma_x2 - soma_x ** 2 / n

sxy = soma_xy - soma_x * soma_y / n

a = sxy / sxx

ym = soma_y / n
xm = soma_x / n

b = ym - a * xm

# calculo coeficiente de regressao
for i in range(len(x)):
    ye = a * x[i] + b
    ve += (ye - ym) ** 2
    vt += (y[i] - ym) ** 2

r2 = ve / vt

print(f'A funcao de regressao e: y = {a:.4f}x + {b:.4f} (R2 = {r2:.4f})')

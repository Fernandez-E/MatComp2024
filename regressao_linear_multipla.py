import numpy as np

x1, x2, y = [], [], []
temp = 0

soma_x1, soma_x2, soma_x12, soma_x22, soma_x1x2, soma_y, soma_x1y, soma_x2y = 0, 0, 0, 0, 0, 0, 0, 0
sxx, sxy = 0, 0

ve, vt = 0, 0

print('Insira os valores para a regressao. Para parar de inserir, digite o valor -9999')

while temp != -9999:
    temp = float(input('Insira um valor para x1: '))
    if temp == -9999:
        break
    x1.append(temp)

    temp = float(input('Insira um valor para x2: '))
    if temp == -9999:
        break
    x2.append(temp)

    temp = float(input('Insira um valor para y: '))
    if temp == -9999:
        x1.pop()
        x2.pop()
        break
    y.append(temp)
    print(f'Valores x1: {x1}')
    print(f'Valores x2: {x2}')
    print(f'Valores y: {y}')

n = len(x1)

# calculo de somatorio utilizando metodo interno de listas:

soma_x1 = sum(x1)
soma_x2 = sum(x2)
soma_y = sum(y)

for i in range(len(x1)):
    soma_x12 += x1[i] ** 2
    soma_x22 += x2[i] ** 2
    soma_x1x2 += x1[i] * x2[i]
    soma_x1y += x1[i] * y[i]
    soma_x2y += x2[i] * y[i]

matrizA = np.array([[n, soma_x1, soma_x2],
                    [soma_x1, soma_x12, soma_x1x2],
                    [soma_x2, soma_x1x2, soma_x22]])

matrizB = np.array([[soma_y],
                    [soma_x1y],
                    [soma_x2y]])

matrizA_inversa = np.linalg.inv(matrizA)

coeficientes = np.dot(matrizA_inversa, matrizB)

b1 = float(coeficientes[1][0])
b2 = float(coeficientes[2][0])
a = float(coeficientes[0][0])

ym = soma_y / n

for i in range(len(x1)):
    ye = a + x1[i]*b1 + x2[i]*b2
    ve += (ye - ym) ** 2
    vt += (y[i] - ym) ** 2

r2 = ve / vt

print(f'A funcao de regressao e: y = {b1:.4f}x1 + {b2:.4f}x2 + {a:.4f} (R2 = {R2:.4f})')

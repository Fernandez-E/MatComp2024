# def gauss_seidel(matriz, dimensao):
    # INSERCAO DE DADOS DE ENTRADA
print('Entrada:')
print('#' * 100)
recorrencia = []

print(f'Escreva a equacao de recorrencia para a variavel x: ')
recorrencia.append(input('>>> ').lower())

print(f'Escreva a equacao de recorrencia para a variavel y: ')
recorrencia.append(input('>>> ').lower())

print(f'Escreva a equacao de recorrencia para a variavel z: ')
recorrencia.append(input('>>> ').lower())

print(f'Indique a inicializacao para a variavel x: ')
x = float(input('>>> '))

print(f'Indique a inicializacao para a variavel y: ')
y = float(input('>>> '))

print(f'Indique a inicializacao para a variavel z: ')
z = float(input('>>> '))

print('Indique o erro admissivel: ')
erroadm = float(input('>>> '))

xtemp = (eval(recorrencia[0]))
ytemp = (eval(recorrencia[1]))
ztemp = (eval(recorrencia[2]))

erroatual1 = abs(x - xtemp)
erroatual2 = abs(y - ytemp)
erroatual3 = abs(z - ztemp)

while erroatual1 > erroadm or erroatual2 > erroadm or erroatual3 > erroadm:
    x = xtemp
    y = ytemp
    z = ztemp

    print(f'x = {x:.2f} ({erroatual1:.4f})| y = {y:.2f} ({erroatual2:.4f}) | z = {z:.2f} ({erroatual3:.4f})')

    xtemp = (eval(recorrencia[0]))
    ytemp = (eval(recorrencia[1]))
    ztemp = (eval(recorrencia[2]))

    erroatual1 = abs(x - xtemp)
    erroatual2 = abs(y - ytemp)
    erroatual3 = abs(z - ztemp)
talude = 0
fy1, fy2 = 0, 0
manning = ''

print('#' * 100)
print(f'DETERMINAÇÃO DE LÂMINA DE ESCOAMENTO EM CANAIS')
print('#' * 100)
print('Para qual tipo de canal que deseja realizar o cálculo?')
print('1 - Retangular')
print('2 - Trapezoidal')
tipo_canal = int(input('>>> '))

if tipo_canal == 1:
    print('#' * 100)
    print(f'DIMENSIONAMENTO DE CANAIS RETANGULARES')
    print('#' * 100)

elif tipo_canal == 2:
    print('#' * 100)
    print(f'DIMENSIONAMENTO DE CANAIS TRAPEZOIDAIS')
    print('#' * 100)

print(f'CARACTERÍSTICAS DO CANAL:')
base = float(input('Base (m): '))
declividade = float(input('Declividade de fundo (m/m): '))
rugosidade = float(input('Rugosidade: '))
if tipo_canal == 2:
    talude = float(input('Z do talude: '))
vazao = float(input('Vazão de interesse (m3/s): '))
eadm = float(input('Insira o erro admissível do problema: '))

y = (rugosidade * vazao / (base * declividade ** (1 / 2))) ** (3 / 5)
print('#' * 100)
print(f'Lâmina estimada inicial por método de canais de bases largas: y = {y:.4f} m')
y1 = float(input('Insira a primeira inicialização da lâmina (m): '))
y2 = float(input('Insira a segunda inicialização da lâmina (m): '))
print('#' * 100)
print('\n')
print('#' * 100)
print(f'APLICAÇÃO DO MÉTODO DAS SECANTES NA EQUAÇÃO DE MANNING')
print('#' * 100)

if tipo_canal == 1:
    manning = "base**(5/3) * y**(5/3) * (2*y+base)**(-2/3) - rugosidade*vazao/(declividade**(1/2))"
    fy1 = eval(manning, {'y': y1, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})
    fy2 = eval(manning, {'y': y2, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})
elif tipo_canal == 2:
    manning = ("declividade**(1/2)/rugosidade * ((base + talude*y) * y) * ((base + talude*y) * y)/(base+2*y*("
               "1+talude**2)**(1/2))**(2/3)-vazao")
    fy1 = eval(manning, {'y': y1, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade, 'talude': talude})
    fy2 = eval(manning, {'y': y2, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade, 'talude': talude})


print(f'y1 = {y1:^10.4f} : f(y1) = {fy1:^10.4f} | y2 = {y2:^10.4f} : f(y2) = {fy2:^10.4f} | erro:   ------')

while abs(y1 - y2) > eadm:
    ytemp = y2
    y2 = (fy2 * y1 - fy1 * y2) / (fy2 - fy1)
    y1 = ytemp

    if tipo_canal == 1:
        manning = "base**(5/3) * y**(5/3) * (2*y+base)**(-2/3) - rugosidade*vazao/(declividade**(1/2))"
        fy1 = eval(manning,
                   {'y': y1, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})
        fy2 = eval(manning,
                   {'y': y2, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})
    elif tipo_canal == 2:
        manning = ("declividade**(1/2)/rugosidade * ((base + talude*y) * y) * ((base + talude*y) * y)/(base+2*y*("
                   "1+talude**2)**(1/2))**(2/3)-vazao")
        fy1 = eval(manning,
                   {'y': y1, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade,
                    'talude': talude})
        fy2 = eval(manning,
                   {'y': y2, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade,
                    'talude': talude})

    print(
        f'y1 = {y1:^10.4f} : f(y1) = {fy1:^10.4f} | y2 = {y2:^10.4f} : f(y2) = {fy2:^10.4f} | erro: {abs(y1 - y2):^10.4f}')

print('#' * 100)
print('\n')
print('#' * 100)
print(f'A lâmina escoada é de {y2:^10.4f} m com um erro associado de {abs(y1 - y2):^10.4f}')
print('#' * 100)

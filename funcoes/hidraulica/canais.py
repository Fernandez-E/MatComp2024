print('#'*100)
print(f'DETERMINAÇÃO DE LÂMINA DE ESCOAMENTO EM CANAIS')
print('#'*100)
print('Para qual tipo de canal que deseja realizar o cálculo?')
print('1 - Retangular')
print('2 - Trapezoidal')
tipo_canal = int(input('>>> '))
if tipo_canal == 1:
    print('#'*100)
    print(f'DIMENSIONAMENTO DE CANAIS RETANGULARES')
elif tipo_canal == 2:
    print('#'*100)
    print(f'DIMENSIONAMENTO DE CANAIS TRAPEZOIDAIS')
print('#'*100)
print(f'CARACTERÍSTICAS DO CANAL:')
base = float(input('Insira a base do canal (m): '))
declividade = float(input('Insira a declividade de fundo do canal (m/m): '))
rugosidade = float(input('Insira a rugosidade do canal: '))
vazao = float(input('Insira a vazão de interesse para a determinação da lâmina de escoamento (m3/s): '))
eadm = float(input('Insira o erro admissível do problema: '))

y = (rugosidade*vazao/(base*declividade**(1/2)))**(3/5)
print('#'*100)
print(f'Lâmina estimada inicial por método de canais de bases largas: y = {y:.4f} m')
y1 = float(input('Insira a primeira inicialização da lâmina (m): '))
y2 = float(input('Insira a segunda inicialização da lâmina (m): '))
print('#'*100)
print('\n')
print('#'*100)
print(f'APLICAÇÃO DO MÉTODO DAS SECANTES NA EQUAÇÃO DE MANNING')
print('#'*100)

manning = "base**(5/3) * y**(5/3) * (2*y+base)**(-2/3) - rugosidade*vazao/(declividade**(1/2))"

fy1 = eval(manning, {'y': y1, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})
fy2 = eval(manning, {'y': y2, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})

print(f'y1 = {y1:^10.4f} : f(y1) = {fy1:^10.4f} | y2 = {y2:^10.4f} : f(y2) = {fy2:^10.4f} | erro:   ------')

while abs(y1 - y2) > eadm:
    ytemp = y2
    y2 = (fy2 * y1 - fy1 * y2) / (fy2 - fy1)
    y1 = ytemp

    fy1 = eval(manning, {'y': y1, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})
    fy2 = eval(manning, {'y': y2, 'base': base, 'rugosidade': rugosidade, 'vazao': vazao, 'declividade': declividade})

    print(f'y1 = {y1:^10.4f} : f(y1) = {fy1:^10.4f} | y2 = {y2:^10.4f} : f(y2) = {fy2:^10.4f} | erro: {abs(y1-y2):^10.4f}')

print('#'*100)
print('\n')
print('#'*100)
print(f'A lâmina escoada é de {y2:^10.4f} m com um erro associado de {abs(y1-y2):^10.4f}')
print('#'*100)

#Entrada
funcao = [] # 0 = funcao, 1 = derivada

print(f'Escreva a função implícita: ')
funcao.append(input('>>> ').lower())

print(f'Escreva a derivada da função implícita: ')
funcao.append(input('>>> ').lower())

print(f'Escreva a inicialização da variavel x: ')
x = float(input('>>> '))

print(f'Indique o erro admissivel: ')
eadm = float(input('>>> '))

fx = eval(funcao[0])
dx = eval(funcao[1])

print(f"xi-1 = {x:10.2f} | f(xi-1) = {fx:10.2f} | f'(x-1) = {dx:10.2f}")

xtemp = x
fxtemp = fx
dxtemp = dx

x = xtemp - (fx/dx)

fx = eval(funcao[0])
dx = eval(funcao[1])

while abs(x - xtemp) > eadm:
    print(f"xi-1 = {x:10.4f} | f(xi-1) = {fx:10.4f} | f'(x-1) = {dx:10.4f} | Erro = {abs(x - xtemp):10.4f}")

    xtemp = x
    fxtemp = fx
    dxtemp = dx

    x = xtemp - (fx / dx)
    fx = eval(funcao[0])
    dx = eval(funcao[1])

print(f"xi-1 = {x:10.4f} | f(xi-1) = {fx:10.4f} | f'(x-1) = {dx:10.4f} | Erro = {abs(x - xtemp):10.4f}\n")

print(f"Raiz aproximada: {x:10.5f} | f(x) = {fx:10.5f}")

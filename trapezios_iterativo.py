from time import sleep

valores_x = []
valores_fx = []
valores_integral = []
erro = 999

intervalo = float(input("Insira o delta X inicial: "))
limite_inferior = float(input("Indique o limite inferior da integral: "))
limite_superior = float(input("Indique o limite superior da integral: "))
eadm = float(input('Informe o erro admissivel: '))

funcao = input("Escreva a funcao: ")

i=limite_inferior
# intervalo = (limite_superior-limite_inferior)/dx
while i <= limite_superior:
    x=i
    valores_x.append(x)
    fx = eval(funcao)
    valores_fx.append(fx)
    i+=intervalo

print('\nValores da funcao:')
for j in range(len(valores_fx)):
    print(f'f({valores_x[j]:8.4f}) = {valores_fx[j]:8.4f}')
    # sleep(0.5)

somatorio = 0
for k in range(len(valores_fx)-1):
    if k == 0:
        continue
    somatorio += valores_fx[k]

integral = intervalo * ((valores_fx[0]/2) + somatorio + (valores_fx[-1]/2))
print(f'Integral: {integral}')
valores_integral.append(integral)

while erro > eadm:
    valores_x = []
    valores_fx = []
    intervalo = intervalo/2
    i = limite_inferior
    # intervalo = (limite_superior - limite_inferior) / dx
    while i <= limite_superior:
        x = i
        valores_x.append(x)
        fx = eval(funcao)
        valores_fx.append(fx)
        i += intervalo

    print('\nValores da funcao:')
    for j in range(len(valores_fx)):
        print(f'f({valores_x[j]:8.4f}) = {valores_fx[j]:8.4f}')
        # sleep(0.1)

    somatorio = 0
    for k in range(len(valores_fx) - 1):
        if k == 0:
            continue
        somatorio += valores_fx[k]

    integral = intervalo * ((valores_fx[0] / 2) + somatorio + (valores_fx[-1] / 2))
    print(f'Integral: {integral}')

    valores_integral.append(integral)

    erro = abs(valores_integral[-1] - valores_integral[-2])

print(f'\nValor da integral calculada numericamente\nI = {valores_integral[-1]:5.4f}\ndx = {intervalo}\nErro = {erro:.4f} < {eadm}')

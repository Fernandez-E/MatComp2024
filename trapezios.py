from time import sleep

valores_x = []
valores_fx = []

intervalo = float(input("Insira o intervalo entre pontos: "))
limite_inferior = float(input("Indique o limite inferior da integral: "))
limite_superior = float(input("Indique o limite superior da integral: "))

funcao = input("Escreva a funcao: ")

i=limite_inferior
while i <= limite_superior:
    x=i
    valores_x.append(x)
    fx = eval(funcao)
    valores_fx.append(fx)
    i+=intervalo

print('\nValores da funcao:')
for j in range(len(valores_fx)):
    print(f'f({valores_x[j]:8.4f}) = {valores_fx[j]:8.4f}')
    sleep(0.5)

somatorio = 0
for k in range(len(valores_fx)-1):
    if k == 0:
        continue
    somatorio += valores_fx[k]

integral = intervalo * ((valores_fx[0]/2) + somatorio + (valores_fx[-1]/2))

print(f'\nValor da integral calculada numericamente: {integral:5.4f}')
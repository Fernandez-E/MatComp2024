valores_x = []
valores_fx = []
resultado = 0

print('Qual grau do polinômio deseja utilizar? [1, 2 ou 3]: ')
grau = int(input('>>> '))

print('Para qual valor deseja interpolar? ')
x_interpolado = float(input('>>> '))

print('Informe os valores x e f(x): ')
i=0
for i in range(grau+1):
    valores_x.append(float(input('x = ')))
    valores_fx.append(float(input(f'f({valores_x[-1]}) = ')))
    print('---')

if grau==1:
    resultado = valores_fx[0]*((x_interpolado-valores_x[1])/(valores_x[0]-valores_x[1])) + valores_fx[1] * ((x_interpolado-valores_x[0])/(valores_x[1]-valores_x[0]))

elif grau==2:
    resultado = valores_fx[0]*((x_interpolado-valores_x[1])/(valores_x[0]-valores_x[1]))*((x_interpolado-valores_x[2])/(valores_x[0]-valores_x[2])) + valores_fx[1] * ((x_interpolado-valores_x[0])/(valores_x[1]-valores_x[0])) * ((x_interpolado-valores_x[2])/(valores_x[1]-valores_x[2])) + valores_fx[2] * ((x_interpolado-valores_x[0])/(valores_x[2]-valores_x[0])) * ((x_interpolado-valores_x[1])/(valores_x[2]-valores_x[1]))
else:
    print('Vai desenvolver')
print(f'Interpolado: P{grau}({x_interpolado}) = {resultado:6.4f}')

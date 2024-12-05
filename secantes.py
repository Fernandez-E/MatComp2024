# Entrada
funcao = []  # 0 = funcao
varx = []
varfx = []

print(f'Escreva a função implícita: ')
funcao.append(input('>>> ').lower())

print(f'Escreva a primeira inicialização da variável x: ')
varx.append(float(input('>>> ')))

print(f'Escreva a segunda inicialização da variável x: ')
varx.append(float(input('>>> ')))

print(f'Indique o erro admissível: ')
eadm = float(input('>>> '))

print(varx)

# Avaliando os dois primeiros pontos
for i in range(2):
    x = varx[i]
    fx = eval(funcao[0], {"x": x})
    varfx.append(fx)
    print(f"{x:10.2f} | f({x:2.2f}) = {varfx[-1]:10.2f}")

# Método das Secantes
while abs(varx[-1] - varx[-2]) > eadm:
    x = (varfx[-1]*varx[-2] - varfx[-2]*varx[-1]) / (varfx[-1]-varfx[-2])
    # x = varx[-1] - (varfx[-1] * (varx[-1] - varx[-2])) / (varfx[-1] - varfx[-2])
    fx = eval(funcao[0], {"x": x})

    varx.append(x)
    varfx.append(fx)

    print(f"{x:10.2f} | f({x:2.2f}) = {varfx[-1]:10.2f} | Erro = {abs(varx[-1] - varx[-2]):10.4f}")

# Resultado final
print(f"Raiz aproximada: {varx[-1]:10.5f} | f(x) = {varfx[-1]:10.5f}")





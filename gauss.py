tamanho_matriz = int(input("Insira o tamanho da matriz quadrada: "))
matriz = []
matriz_resultado = []

for x in range(tamanho_matriz):
    matriz.append([])
    print(f'Indique os valores da linha {x+1} da matriz')
    for y in range(tamanho_matriz):
        matriz[x].append(float(input('>>> ')))

for linha in matriz:
    print(linha)

print('Informe os valores da matriz resultado')
for x in range(tamanho_matriz):
    matriz_resultado.append(float(input('>>> ')))

for linha in matriz_resultado:
    print(linha)


i = 0
while i < tamanho_matriz - 1:
    pivo = matriz[i][i]
    for k in range(i + 1, tamanho_matriz):
        multiplicador = -matriz[k][i] / pivo
        matriz_resultado[k] += multiplicador * matriz_resultado[i]
        for j in range(len(matriz[k])):
            matriz[k][j] += multiplicador * matriz[i][j]
    i += 1

for linha in matriz:
    print(linha)

for linha in matriz_resultado:
    print(linha)


resultados = []
resultados.append(matriz_resultado[2] / matriz[2][2])
resultados.append((matriz_resultado[1] - matriz[1][2] * resultados[0]) / matriz[1][1])
resultados.append((matriz_resultado[0] - matriz[0][2] * resultados[0] - matriz[0][1] * resultados[1]) / matriz[0][0])
print(resultados)



import matplotlib.pyplot as plt
from time import sleep

x, fx, dx2 = [], [], []
temp = 0
t, r = 0, 0

fx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 2
r = 3
#
# while temp != -9999:
#     temp = float(input('Insira um valor para x: '))
#     if temp == -9999:
#         break
#     x.append(temp)
#     temp = float(input('Insira um valor para fx: '))
#     if temp == -9999:
#         x.pop()
#         break
#     fx.append(temp)

dx = x[0] - x[1]

# t = float(input("Insira o valor de transmissividade: "))
# r = float(input("Insira o valor de recarga: "))

k = 0
while k < 100:
    dx2 = []
    i = 1
    while i < len(x) - 1:
        derivada = 1/2*(fx[i+1]+fx[i-1]+(r*dx**2/t))
        dx2.append(derivada)
        i += 1
    j = 1
    while j < len(fx)-1:
        fx[j] = dx2[j-1]
        j += 1
    print(fx)

    k += 1
    plt.plot(x, fx)
    plt.ylim(0, 20)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")

plt.show()
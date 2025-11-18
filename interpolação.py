x = []
y = []
l = []
n = int(input("Qual o número de pontos desejado? "))
xint = float(input("Para qual valor deseja interpolar? "))

i = 0
print('Insira os valores conhecidos para x e y.')
while i < n:
    x.append(float(input("x: ")))
    y.append(float(input("y: ")))
    i += 1

k = 0
for k in range(0, n):
    num = 1
    den = 1
    i = 0
    for i in range(0, n):
        if i != k:
            num *= (xint - x[i])
            den *= (x[k] - x[i])
    l.append(num/den)

p = 0
for i in range(len(l)):
    p += l[i]*y[i]

print(f'O valor interpolado para x = {xint} é y = {p:.2f}')

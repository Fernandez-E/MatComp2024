x, fx, dx2 = [], [], []
temp = 0

while temp != -9999:
    temp = float(input('Insira um valor para x: '))
    if temp == -9999:
        break
    x.append(temp)
    temp = float(input('Insira um valor para fx: '))
    if temp == -9999:
        x.pop()
        break
    fx.append(temp)

dx = x[0] - x[1]

i=1
while i < len(x) - 1:
    derivada = (fx[i+1] - 2*fx[i] + fx[i-1]) / (dx ** 2)
    dx2.append(derivada)
    i += 1

for item in dx2:
    print(item)


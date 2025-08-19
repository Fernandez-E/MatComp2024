def fatorial(numero):
    fat = 1
    while numero >= 1:
        fat *= numero
        numero -= 1
    return fat

def fatorial_rec(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial_rec(numero-1)

print(fatorial_rec(10))
print(fatorial(6))


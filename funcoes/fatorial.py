def fatorial(numero):
    fatorial = 1
    while numero > 0:
        fatorial = fatorial * numero
        numero -=1
    return fatorial

for i in range(5): print(fatorial(i))
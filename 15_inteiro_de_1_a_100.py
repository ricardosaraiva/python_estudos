import random

numeros = []
for i in range(15):
    x = random.randint(10, 100)
    if x not in numeros:
        numeros.append(x)
    
print(numeros)
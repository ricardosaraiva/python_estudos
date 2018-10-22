numeros= [10, 30, 45, 5 , 64, 14, 2, 7, 10, 6, 43, 100,8]
i = 0

par = []
impar = []

while i < 13:
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])
    i += 1
    
print("par %s" %par)
print("impar %s" %impar)
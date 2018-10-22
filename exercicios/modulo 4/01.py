numeros= [10, 30, 45, 5 , 64, 14, 2, 5, 10, 6]
i = 0
maiorValor = 0

while i <= 9:
    if maiorValor < numeros[i]:
        maiorValor = numeros[i]    
    i += 1 
    
print("O maior valor é %d" %maiorValor)
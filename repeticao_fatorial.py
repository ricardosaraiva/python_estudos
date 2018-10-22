valor = int(input("Fatorial de"))
calc = valor

while valor > 1:
    valor = valor - 1
    calc = calc * valor
    
print(calc)
numero = 1;

while numero <= 10:
    multiplicador = 1
    print('tabuada do %d' %numero)
    while multiplicador <= 10 :
        print('%d x %d = %d' %(numero, multiplicador, numero * multiplicador))
        multiplicador = multiplicador + 1
    numero = numero + 1
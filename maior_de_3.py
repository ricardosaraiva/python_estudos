numero1 = int(input("1º numero"))
numero2 = int(input("2º numero"))
numero3 = int(input("3º numero"))

if(numero1 >= numero2 and numero1 >= numero3):
    print('1º numero é o maio')
elif(numero2 >= numero1 and numero2 >= numero3):
    print('2º numero é o maio')
else:
    print('3º numero é o maio')
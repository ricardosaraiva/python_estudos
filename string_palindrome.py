palavra = input("digite uma palavra ")

if(palavra == palavra[::-1]) :
    print("É um palindrome")
else:
    print("Não é um palindrome")
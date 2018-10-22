palavra = input("palavra")
novaPalavra =  ''
i = 0

while  i < len(palavra):
    if palavra[i] in 'aeiou':
        novaPalavra = novaPalavra + '*'
    else:
        novaPalavra = novaPalavra + palavra[i]
        
    i += 1
    
print(novaPalavra)
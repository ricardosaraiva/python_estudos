conteudo = ''
with open('read.txt') as f:
    conteudo = f.read()
    
for letra in ['a', 'e', 'i', 'o', 'u']:
    conteudo = conteudo.replace(letra, '*')

salvar = open('write.txt', 'w')
salvar.write(conteudo)
salvar.close();
x = "Ricardo Saraiva"

#substring

#inicio
print(x[0:7])
print(x[0:1])
print(x[:7])# pega os primeiros sete caracteres

#final
print(x[-1]) #pega o ultimo caractere
print(x[-7:]) #pega os ultimos 7 caracteres

#pegar posição multiplar do valor informado
print(x[::2]) #pega somentes os caracteres multiplos de 2

#inverter string
print(x[::-1])
print(x[::-2]) #inverte a string pegando somente os caracteres pares

#conveter string
print(x.lower()) #converter uma string para minusculo
print(x.upper()) #converte uma string para maisculo

#busca em string
print(x.startswith('R'))# valida se uma string inicia com o valor informado
print(x.endswith('v'))# valida se uma string termina com o valor informado
print(x.find('ca')) # busca por valor em uma string e retorna sua posição
print(x.find('r', 7)) # busca por valor em uma string a partir de um ponto
print(x.replace('a', '*')) # busca pelo valor informado e substitui por outro valor

#quebra string e converter em lista
print(x.split()) # quebra uma string se não for informado parametro quebra por espaço
print('10/10/2018'.split('/')) #quebra uma string baseado no caractere informado

#junta todos os itens da lista em string
print('/'.join(['10', '10', '2016'])) # junta os itens da lista em um string 

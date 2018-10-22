import math

area = int(input("Tamanho da area a ser pintada?"))
lataLitros = 18
litrosMetro = 3
metrosPorLata =  lataLitros * litrosMetro

latasUsadas = math.ceil(area / metrosPorLata)

print("Total de latas: %d" % latasUsadas)    
print("Valor total: R$ %6.2f" %( latasUsadas * 80))    
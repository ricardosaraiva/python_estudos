minutos = int(input("Quantos minutos você gastou?"))

if minutos >= 800 :
    tarifa = 0.08
elif minutos > 400:
    tarifa = 0.15
elif minutos > 200 :
    tarifa = 0.18
else :
    tarifa = 0.20
    
print("Conta telefonica: R$%6.2f" %(tarifa * minutos) )
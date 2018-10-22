velocidade = int(input("Testar velocidade?"))

if velocidade > 110: 
    multa = (velocidade - 110) * 5
    print("Valor da multa R$: %5.2f " %multa)
data = input("data de nascimento ")

mes = []
mes.append('janeiro')
mes.append('fevereiro')
mes.append('março')
mes.append('abril')
mes.append('maio')
mes.append('junho')
mes.append('julho')
mes.append('agosto')
mes.append('setembro')
mes.append('outubro')
mes.append('novenbro')
mes.append('dezenbro')


quebraData = data.split('/')
mesAtual = int(quebraData[1]) - 1
print(mes[mesAtual])
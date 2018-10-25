import random

palavra = list(input('Palavra '))
random.shuffle(palavra)

print(''.join(palavra))
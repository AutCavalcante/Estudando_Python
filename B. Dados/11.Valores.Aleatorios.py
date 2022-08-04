############### 11 - VALORES ALEATÓRIOS ###############
'''
IMPORTÂNCIA:
PODE SER UTILIZADO PARAS AS MAIS DIFERENTES FINALIDADES, TAIS COMO:
    - CRIAÇÃO DE SENHAS;
    - TESTES ESTATÍSTICOS, ENTRE OUTROS.

    EXEMPLOS
'''

import random
'''
# IMPRIMIR VALORES ALEATÓRIOS ENTRE O E 1
'''
print(random.random())

'''
IMPRIMIR VALORES ALEATÓRIOS ENTRE UM INTERVALO QUALQUER
'''
print(random.uniform(5, 25))

'''
IMPRIMIR VALORES INTEIROS E ALEATÓRIOS ENTRE UM INTERVALO QUALQUER
'''
print(random.randint(5, 25))

'''
EMBARALHAR VALORES
'''
cartas = ['copas', 'paus', 'espadas', 'ouros']
print(random.shuffle(cartas))
print(cartas)
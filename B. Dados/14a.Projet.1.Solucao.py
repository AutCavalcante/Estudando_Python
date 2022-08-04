############### 🥇 PROJETO 1 🥇 ############### 
'''
Módulo 1 - Gerar registro do funcionário
Funcionalidades do módulo 1
'''
    # 1. Obtenha o nome do usuário

from datetime import datetime
import random

userName = input('Cadastre um nome de usuário: ')

    # 2. Obtenha a idade do usuário

userAge = int(input('Idade: '))
print(type(userAge))


    # 3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

dataRegistration_d = datetime.now().day
dataRegistration_m = datetime.now().month
dataRegistration_y = datetime.now().year

    # 4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:

cartoes = ['R$50,00','R$250,00','R$120,00']
sorteioCartao = random.choice(cartoes)

    # 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
dataBirthday = datetime.strptime(input('Insira a data do seu aniversário no formato DD/MM/AAAA: '),  '%d/%m/%Y')

'''
Módulo 2 - Gerar apresentação do usuário
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

    1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
    Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''

print(f'''Olá {userName}, seu registro foi concluído com sucesso no dia {dataRegistration_d}/{dataRegistration_m}/{dataRegistration_y}.
Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteioCartao}.''')
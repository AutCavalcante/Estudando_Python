

from datetime import datetime
import random
import os
    
#1. Obtenha o nome do usuário
nome = input('Digite o nome do funcionário: ')
    
#2. Obtenha a idade do usuário
idade = input('Digite a idade do funcionário: ')
    
#3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
data = datetime.today().strftime('%d-%m-%Y')
    
#4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
cartoes = ['R$50,00','R$250,00','R$120,00']
sorteio = random.choice(cartoes)
#5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
data_aniversario = datetime.strptime(input('Digite a data de aniversário do funcionário: '),'%d/%m/%Y')
## Módulo 2 - Gerar apresentação do usuário
os.system("cls")
### Funcionalidades do módulo 2 - Mensagem de boas vindas!
print(f'Cadastro efetuado com sucesso!! Seja Bem vindo {nome}')
print('='*80)
#Usando os dados obtidos no módulo 1, exiba as seguintes informações:
    
#1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data}')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}')
print('='*80)

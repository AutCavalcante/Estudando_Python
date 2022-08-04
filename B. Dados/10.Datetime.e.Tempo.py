############### 10 - DATETIME E TEMPO ###############
'''
SERVE PARA QUE VOCÊ DECIDA QUANDO UM PROGRAMA DEVA RODAR E MUITO MAIS.
        EXEMPLOS
'''
from datetime import datetime

print(datetime.now()) # DETERMINE O HORÁRIO EXATO NESTE MOMENTO
print(datetime.now().day) # DETERMINE O DIA DE HOJE
print(datetime.now().month) # DETERMINE O MÊS QUE ESTAMOS
print(datetime.now().year) # DETERMINE O ANO QUE ESTAMOS

data_casamento = datetime(2015, 10, 9) # CRIANDO UMA DATA
print(data_casamento)

data_casamento = input('Insira a data do seu casamento: ') # RECEBENDO A DATA DE CASAMENTE De ALGUÉM
print(data_casamento)
print(type(data_casamento))

data_casamento = input('Insira a data do seu casamento: ') # CONVERTENDO O TIPO DO datetime PARA datetime
data_casamento = datetime.strptime(input('Insira a data do seu casamento: ', '%d'/%m'/'%Y)
print(type(data_casamento))

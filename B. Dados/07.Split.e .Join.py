############### 07 - SPLIT E JOIN ###############
'''
IMPORTANTE PARA SEPARAR UMA STRING EM PARTES
    EXEMPLOS DE COMO QUEBRAR STRINGS
'''
from http.client import MULTI_STATUS


frase = 'Olá, bem-vindo a esse treinamento!'
'''
    1º SEPARA A STRING APENAS ONDE EXISTE ESPAÇO E GUARDA AS PARTES EM UMA LISTA
'''
print(frase.split())
'''
    2º SEPARA A STRING APENAS ONDE EXISTE VIRGULA E GUARDA AS PARTES EM UMA LISTA
'''
print(frase.split(','))
'''
    3º SEPARA A STRING APENAS ONDE EXISTE VIRGULA E GUARDA AS PARTES EM UMA LISTA
'''
print(frase.split('-'))

nomes = 'Pedro, Dennis, Erivaldo, Bruno,Oswaldo'
'''
OBS 1.: A FUNÇÃO STRIP PODE IDENTIFICAR NA STRING A VÍRGULA OU OUTRO SÍMBOLO, MESMO QUE NÃO EXISTA ESPAÇO LOGO APÓS ELES
'''
print(nomes.split())
print(nomes.split(','))
'''
OBS 2.: A FUNÇÃO STRIP PODE POSSUIR 2 ARGUMENTOS, TIPO: STRIP('SEPARADOR', Nº DE OCORRÊNCIAS)
'''
hashtags = 'Pedro, #Dennis, #Erivaldo, #Bruno, #Oswaldo'
print(hashtags.split())
print(hashtags.split("#"))
print(hashtags.split('#', 3)) # SEPARADOR ('#'), Nº DE OCORRÊNCIAS (2)

'''
    EXEMPLOS DE COMO JUNTAR/CONCATENAR STRINGS
'''
musicas = 'Sertenejo Rock Forro Tango Carimbo'
var_espaco = musicas.split(' ')
print(var_espaco)

print('; '.join(var_espaco))
print('-'.join(var_espaco))
print('. '.join(var_espaco))


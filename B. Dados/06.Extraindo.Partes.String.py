############### 05 - EXTRAINDO PARTES DE UMA STRINGS ###############
'''
IMPORTANTE PARA IDENTIFICAR O INDEX E EXTRAIR PARTES DE UMA STRING
    EXEMPLO  
'''
var_1 = 'PalavraGigante'

print(var_1[4]) # IMPRIME A LETRA CORRESPONDENTE AO INDEX 4
print(var_1[-1]) # IMPRIME A ÚLTIMA LETRA DA STRING
print(var_1[0:3]) # IMPRIME DO INDEX 0 AO INDEX 2 (SEMPRE ULTIMO VALOR -1)
print(var_1[2:]) # IMPRIME DO INDEX 2 AO FIM DA STRING
print(var_1[-2:]) # IMPRIME DO INDEX -2 AO FIM DA STRING
print(var_1[:-3]) # IMPRIME DO INDEX 0 AO INDEX -3
print(var_1.index('a'))
print(var_1.rindex('a'))
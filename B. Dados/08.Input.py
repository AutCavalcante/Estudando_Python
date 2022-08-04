############### 08 - INPUT ###############
'''
IMPORTÂNCIA:
    PARA PARA O USUÁRIO ENTRAR COM UMA INFORMAÇÃO;
    A INFORMAÇÃO INSERIDA SEMPRE SERÁ CONVERTIDA PARA STRING
'''

idade = input('ESCREVA A SUA IDADE NO CAMPO ABAIXO: ')
print(type(idade))

'''
DEPENDENDO DO TIPO DE INFORMAÇÃO PODE SER NECESSÁRIO FAZER A CONCERSÃO DO TYPE
'''
idade = int(input('ESCREVA A SUA IDADE NO CAMPO ABAIXO: '))
print(type(idade))
nascimento = (2022-idade)
print(f'Você nasceu em: {nascimento}')

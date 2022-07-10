############### 04 - STRINGS ###############
'''
SÃO INFORMAÇÕES CONSTITUIDAS GERALMENTE POR TEXTO E SÍMBOLOS, MAS QUE PODE CONTER NÚMEROS

FORMAS DE IMPRIMIR UMA STRING
    SERVE PARA INSERIR CARACTERES 'ILEGAIS' EM UMA STRING
    EXEMPLO
'''
print('Vamos aprender Python! O importante é codar!') # UTILIZANDO ASPAS SIMPLES
print("Vamos aprender Python! O importante é codar!") # UTILIZANDO ASPAS DUPLAS
print('''Vamos aprender Python!
O importante é codar!''') # UTILIZANDO ASPAS TRIPLAS, QUANDO A ESTRING POSSUI MAIS DE UMA ALINHA
print("""Vamos aprender Python!
O importante é codar!""") # UTILIZANDO ASPAS TRIPLAS, QUANDO A ESTRING POSSUI MAIS DE UMA ALINHA

'''
LISTA DE CARACTERES DE ESCAPE
ESCAPE      RESULTADO
\'	        Single Quote	
\\	        Backslash	
\n	        New Line	
\t	        Tab	
\b	        Backspace	

    EXEMPLO
'''
print('Olá! Meu nome é: \nPedro.') # CONDICIONA A CRIAÇÃO DE UMA NOVA LINHA PARA O TEXTO POSTERIOR AO CARACTERE DE ESCAPE
print('Sua marca d\'água.') # A BARRA INVERTIDA PERMITE INSERIR CARACTERES ILEGAIS EM UMA STRING
print('Localize o arquivo: c:\\arquivo1.txt')

'''
STRINGS PODEM SER GUARDADAS DENTRO DE VARIÁVEIS
    EXEMPLO
'''
idade = '26'
print(idade)

'''
CONTANDO OS CARACTERES DE UMA STRING
'''
print(len(idade))

'''
DICAS

1 PARA COMENTAR UMA LINHA
    CTRL + K + C

2 RETIRAR UM COMENTÁRIO
    CTRL + K + U

3 COMENTAR OU DESCOMENTAR VÁRIAS LINHAS
    SHIFT + ALT + A
'''


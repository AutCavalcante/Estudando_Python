############### 13 - DEBUGANDO CÓDIGOS ###############
'''
IMPORTÂNCIA:
    NEM TODO ERRO VOCÊ VAI ENCONTRAR EM UMA PESQUISA NO GOOGLE, APENAS OS DE SINTAXE;
    ERROS DE LÓGICA PRECISAM SER DEBUGADOS.

    EXEMPLO:
'''
print('Olá')
'''
    1. CRIE UM BREAK POINT 
        # F9
'''
def calcular_preco_combo(pizza, refrigerante):
    total = pizza + refrigerante
    print(total)

calcular_preco_combo(30, 'vinte reais')
print('Programa finalizado!')
'''
    2. ATIVE O MODO DEBUGE
        # F5 -> PYTHON FILE
    
    3. ENTRANDO EM UMA FUNÇÃO
        # UTILIZE O PANEL DEBUG PARA RODAR LINHA POR LINHA (F10)
    
    4. FAÇA AS ATERAÇÕES NECESSÁRIAS PARA COROIGIR O CÓDIGO!
'''
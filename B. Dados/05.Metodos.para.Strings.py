############### 05 - MÉTODOS PARA STRINGS ###############
'''
SERVE PARA RESUMIR TAREFAS CHATAS, MAS IMPORTANTES
    EXEMPLO  
'''
var_1 = ' sEU MALA!  Só não deve deixar espaços nesse campo! bAbACA!!!      '

print(var_1.upper()) # FONTE MAIÚSCULA
print(var_1.lower()) # FONTE MINÚSCULA

print(var_1.rstrip()) # REMOVENDO ESPAÇOS EM BRANCO À DIREITA DA STRING
print(var_1.lstrip()) # REMOVENDO ESPAÇOS EM BRANCO À ESQUERDA
print(var_1.strip())  # REMOVENDO ESPAÇOS EM BRANCO À DIREITA E À ESQUERDA

print(var_1.strip().rstrip('bAbACA!!!')) # 3.REMOVENDO INSULTO À DIREITA DA STRING
print(var_1.strip().lstrip('sEU MALA!')) # REMOVENDO INSULTO À ESQUERDA
print(var_1.strip().lstrip('sEU MALA!').rstrip('bAbACA!!!').upper()) # 3.REMOVENDO INSULTO À DIREITA E À ESQUERDA
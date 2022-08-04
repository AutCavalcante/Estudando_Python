######## 🥇 RESOLUÇÃO - MÉTODOS PARA STRINGS 🥇 ########
'''
    ENCONTRE O ÍNDICE 'a' DENTRO DA VARIÁVEL var_1     
'''
var_1 = 'Inconstitucional'

print(var_1.index('a'))

'''
USANDO AS PALAVRAS
'Automação para Desenvolvimento Institucional'
IMPRIMA APENAS AS PLAVRAS 'Desenvolvimento Institucional'
'''
frase = 'Automação para Desenvolvimento Institucional'
print(frase[-29:]) # PRECISA CONTAR O INDEX

index_d = frase.rindex('D') # DESCOBRINDO O INDEX AUTOMATICAMENTE
print(frase[index_d:])
index_l = frase.rindex('l') # DESCOBRINDO O INDEX AUTOMATICAMENTE
print(frase[index_d:index_l+1])

print(var_1.rstrip()) # REMOVENDO ESPAÇOS EM BRANCO À DIREITA DE UM GENE
print(var_1.lstrip()) # REMOVENDO ESPAÇOS EM BRANCO À ESQUERDA
print(var_1.strip())  # REMOVENDO ESPAÇOS EM BRANCO À DIREITA E À ESQUERDA

print(var_1.strip().rstrip('TTT')) # 3.REMOVENDO CODONÀ DIREITA  DE UM GENE
print(var_1.strip().lstrip('AaA')) # REMOVENDO CODON À ESQUERDA
print(var_1.strip().lstrip('AaA').rstrip('TTT')) # 3.REMOVENDO CODONS À DIREITA E À ESQUERDA
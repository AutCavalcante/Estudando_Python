######## 🥇 RESOLUÇÃO - SPLIT E JOIN 🥇 ########

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'
'''
    1. TRANSFORME A frase1 EM UMA LISTA DE PALAVRAS E GUARDE O RESULTADO EM UMA VARIÁVEL CHAMADA palavras1
'''
palavras1 = frase1.split()
print(palavras1)
'''
    2. TRANSFORME A frase2 EM UMA LISTA DE PALAVRAS E GUARDE O RESULTADO EM UMA VARIÁVEL CHAMADA palavras2
'''
palavras2 = frase2.split(',')
print(palavras2)
''' 
    3. PEGUE palavras1 E TRANSFORME ELAS NA SEGUINTE STRING: 'Desafio,manipulação,de,strings'. IMPRIMA O RESULTADO NOCONSOLE.
'''
print(','.join(palavras1))
'''
    4. PEGUE palavras2 E TRANSFORME ELAS NA SEGUINTE STRING: frase2 = "jhonatan & rafael & carol & camilla". IMPRIMA O RESULTADO NO CONSOLE
'''
print(' & '.join(palavras2))
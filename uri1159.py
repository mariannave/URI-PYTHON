avaliador = True
while avaliador:
    numero = int(input())
    soma = 0
    if numero == 0:
        avaliador = False
        break
    if numero % 2 == 0:
        for c in range(0,5):
            soma += numero
            numero += 2
    elif numero % 2 == 1:
        numero += 1
        for c in range(0,5):
            soma += numero
            numero += 2
    print(soma)
    
    
    '''
    Entrada: 
4
11
0
    Saída: 
40
80

'''

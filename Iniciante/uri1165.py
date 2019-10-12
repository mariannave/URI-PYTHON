def primo(n):
    if (n == 2):
        return 1
    if (n == 0 or n == 1 or (n % 2 == 0)):
        return 0
    for i in range(3, int(n**(1/2)) + 2):
        if (n % i == 0):
            return 0
    return 1
quant_de_testes = int(input())
for c in range(0,quant_de_testes):
  numero = int(input())
  if primo(numero):
    print("{} eh primo".format(numero))
  elif not primo(numero):
    print("{} nao eh primo".format(numero))
    
    
    '''
    Entrada: 
3
8
51
7
    Saída:
8 nao eh primo
51 nao eh primo
7 eh primo


'''
  

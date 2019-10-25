'''
Entrada:
3
Saída:
N[0] = 0
N[1] = 1
N[2] = 2
N[3] = 0
N[4] = 1
N[5] = 2
N[6] = 0
N[7] = 1
N[8] = 2
...
'''

valor = int(input())
contagem = 0
for c in range(0,1000):
  print("N[{}] = {}".format(c,contagem))
  contagem += 1
  if contagem == valor:
    contagem = 0

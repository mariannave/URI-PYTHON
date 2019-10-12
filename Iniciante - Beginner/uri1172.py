vetor = []
for c in range(10):
  numero = int(input())
  if numero <= 0:
    numero = 1
  vetor.append(numero)
for c in range(10):
  print("X[{}] = {}".format(c,int(vetor[c])))

  
  '''
  Entrada:
0
-5
63
0
...
Saída:
X[0] = 1
X[1] = 1
X[2] = 63
X[3] = 1
...
'''

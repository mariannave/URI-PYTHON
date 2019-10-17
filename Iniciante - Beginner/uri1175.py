'''
Entrada:
0
-5
...
63
230

Saída:
N[0] = 230
N[1] = 63
...
N[18] = -5
N[19] = 0
'''

vetor = [None] * 20
for c in range(1,21):
  numero = int(input())
  vetor[20-c] = numero
for c in range(20):
  print("N[{}] = {}".format(c,vetor[c]))

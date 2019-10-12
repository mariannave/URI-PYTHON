'''
  Entrada: 7 14 106
  Saída: 106 eh o maior
  -----------------
  Entrada: 217 14 6
  Saída: 217 eh o maior
'''

import math

valor = input().split(" ")
a, b, c = valor
maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2
print("%d eh o maior" %resultado)

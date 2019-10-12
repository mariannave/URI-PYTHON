'''
  Entrada:  1.0 7.0
            5.0 9.0
  Saída: 4.4721
  -----------------
  Entrada:  -2.5 0.4
            12.1 7.3
  Saída: 16.1484
  -----------------
  Entrada:  2.5 -0.4
            -12.2 7.0
  Saída: 16.4575
'''

import math

linha1 = input().split(" ")
linha2 = input().split(" ")
x1,y1 = linha1
x2,y2 = linha2
distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
print("%0.4f" %distancia)

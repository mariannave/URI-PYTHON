'''
  Entrada:  5
            6
            7
            8
  Saída: DIFERENCA = -26
  -----------------
  Entrada:  0
            0
            7
            8
  Saída: DIFERENCA = -56
  -----------------
  Entrada:  5
            6
            -7
            8
  Saída: DIFERENCA = 86
'''

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
diferenca = (n1 * n2) - (n3 * n4)
print("DIFERENCA = %d" %diferenca)

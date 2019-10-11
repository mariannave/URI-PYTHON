'''
  Entrada:  5.0
            6.0
            7.0
  Saída: MEDIA = 6.3
  -----------------
  Entrada:  5.0
            10.0
            10.0
  Saída: MEDIA = 9.0
  -----------------
  Entrada:  10.0
            10.0
            5.0
  Saída: MEDIA = 7.5
'''

n1 = float(input())
n2 = float(input())
n3 = float(input())
soma = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
print("MEDIA = %0.1f" %soma)

'''
  Entrada:  5.0
            7.1
  Saída: MEDIA = 6.43182
  -----------------
  Entrada:  0.0
            7.1
  Saída: MEDIA = 4.84091
  -----------------
  Entrada:  10.0
            10.0
  Saída: MEDIA = 10.00000
'''

nota1 = float(input())
nota2 = float(input())

media = (((nota1 * 3.5) + (nota2 * 7.5)) / 11)

print("MEDIA = %0.5f" %media)

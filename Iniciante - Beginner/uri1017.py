'''
  Entrada: 10
           85
  Saída: X = 70.833
  -----------------
  Entrada: 2
           92
  Saída: X = 15.333
  -----------------
  Entrada: 22
           67
  Saída: X = 122.833
'''

tempo = int(input())
velocidade = int(input())

litros = (velocidade * tempo) / 12

print("%.3f" %litros)

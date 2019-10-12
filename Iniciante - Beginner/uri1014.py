'''
  Entrada:  500
            35.0
  Saída: 14.286 km/l
  -----------------
  Entrada:  2254
            124.4
  Saída: 18.119 km/l
  -----------------
  Entrada:  4554
            464.6
  Saída: 9.802 km/l
'''

distancia = int(input())
combustivel = float(input())
consumo = distancia / combustivel
print("%0.3f km/l" %consumo)

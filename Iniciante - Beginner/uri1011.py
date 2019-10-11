'''
  Entrada: 3
  Saída: VOLUME = 113.097
  -----------------
  Entrada: 15
  Saída: VOLUME = 14137.155
  -----------------
  Entrada: 1523
  Saída: VOLUME = 14797486501.627
'''

raio = int(input())
pi = 3.14159
volume = float(4.0 * pi * (raio* raio * raio) / 3)
print("VOLUME = %0.3f" %volume)

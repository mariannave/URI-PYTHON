'''
  Entrada: 3.0 4.0 5.2
  Saída:  TRIANGULO: 7.800
          CIRCULO: 84.949
          TRAPEZIO: 18.200
          QUADRADO: 16.000
          RETANGULO: 12.000
  -----------------
  Entrada: 12.7 10.4 15.2
  Saída:  TRIANGULO: 96.520
          CIRCULO: 725.833
          TRAPEZIO´: 175.560
          QUADRADO: 108.160
          RETANGULO: 132.080
'''

valor = input().split(" ")
a, b, c = valor
pi = 3.14159
triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)
print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))

'''
  Entrada:  12 1 5.30
            16 2 5.10
  Saída: VALOR A PAGAR: R$ 15.50
  -----------------
  Entrada:  13 2 15.30
            161 4 5.20
  Saída: VALOR A PAGAR: R$ 51.40
  -----------------
  Entrada:  1 1 15.10
            2 1 15.10
  Saída: VALOR A PAGAR: R$ 30.20
'''

linha1 = input().split(" ")
linha2 = input().split(" ")
cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2
total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))
print("VALOR A PAGAR: R$ %0.2f" %total)

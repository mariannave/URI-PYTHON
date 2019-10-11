'''
  Entrada:  JOAO
            500.00
            1230.30
  Saída: TOTAL = R$ 684.54
  -----------------
  Entrada:  PEDRO
            700.00
            0.00
  Saída: TOTAL = R$ 700.00
  -----------------
  Entrada:  MANGOJATA
            1700.00
            1230.50
  Saída: TOTAL = R$ 1884.58
'''

nome = input()
salfixo = float(input())
qtdevendas = float(input())
bonus = float(qtdevendas * (15/100))
total = salfixo + bonus
print("TOTAL = R$ %0.2f" %total)

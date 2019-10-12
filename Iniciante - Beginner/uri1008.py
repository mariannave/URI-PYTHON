'''
  Entrada:  25
            100
            5.50
  Saída:  NUMBER = 25
          SALARY = U$ 550.00
  -----------------
  Entrada:  1
            200
            20.50
  Saída:  NUMBER = 1
          SALARY = U$ 4100.00
  -----------------
  Entrada:  6
            145
            15.55
  Saída:  NUMBER = 6
          SALARY = U$ 2254.75
'''

numfunc = int(input())
hrtrab = int(input())
valorhr = float(input())
salario = float(hrtrab * valorhr)
print("NUMBER = %d" %numfunc)
print("SALARY = U$ %0.2f" %salario)

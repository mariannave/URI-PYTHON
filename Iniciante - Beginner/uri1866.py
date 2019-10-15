'''
Entrada:
3
11
7
18
Saída:
1
1
0
'''

quant_de_testes = int(input())
for c in range(quant_de_testes):
  numero = int(input())
  if numero % 2 == 0:
    print(0)
  elif numero % 2 == 1:
    print(1)
  

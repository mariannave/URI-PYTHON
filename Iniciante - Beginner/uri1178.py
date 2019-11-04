'''
Entrada:
200.0000
Saída:
N[0] = 200.0000
N[1] = 100.0000
N[2] = 50.0000
N[3] = 25.0000
N[4] = 12.5000
...

'''
valor = float(input())
for c in range(100):
  print("N[{}] = {:.4f}".format(c,valor))
  valor = valor / 2

'''
Entradas: 
3
8 12
9 27
259 111
Saída:
4
9
37
'''
def mdc(a,b):
  if a % b == 0:
    return b
  else:
    return mdc(b,a % b)
quant_de_testes = int(input())
for c in range(quant_de_testes):
  a = input().split(" ")
  numero1 = int(a[0])
  numero2 = int(a[1])
  print(mdc(numero1,numero2))

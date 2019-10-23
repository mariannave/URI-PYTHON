'''
Entrada:
S
1.0
0.0
-3.5
2.5
4.1
Saída:
12.6
...
'''



soma_ou_media = input()
soma = 0
for i in range(12):
  for j in range(12):
    elem = float(input())
    if i + j <= 10:
      soma += elem
if soma_ou_media == "S":
  print("{:.1f}".format(soma))
elif soma_ou_media == "M":
  print("{:.1f}".format(soma / 66))

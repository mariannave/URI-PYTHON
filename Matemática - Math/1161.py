'''
Entradas:
4 4
0 0
0 2
Saídas:
48
2
3
'''


while True:
  try:
    numeros = input().split(" ")
    numero1 = int(numeros[0])
    numero2 = int(numeros[1])
    soma1 = 1
    soma2 = 1
    for c in range(1,numero1 + 1):
      soma1 = soma1 * c
    for c in range(1,numero2 + 1):
      soma2 = soma2 * c
    print(soma1 + soma2) 
  except EOFError:
    break


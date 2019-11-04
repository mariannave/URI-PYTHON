'''
Entrada:
5
4A5
3A3
4f2
2G4
7Z1

Saída:
1
9
6
2
-6
'''

quant_de_testes = int(input())
for c in range(quant_de_testes):
  entrada = input()
  digito1 = int(entrada[0])
  letra1 = entrada[1]
  digito2 = int(entrada[2])
  if digito1 == digito2:
    print(digito1 * digito2)
  elif letra1.isupper():
    print(digito2 - digito1)
  elif letra1.islower():
    print(digito1 + digito2)
  

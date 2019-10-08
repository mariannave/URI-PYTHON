vetor = []
for c in range(10):
  numero = int(input())
  if numero <= 0:
    numero = 1
  vetor.append(numero)
for c in range(10):
  print("X[{}] = {}".format(c,int(vetor[c])))

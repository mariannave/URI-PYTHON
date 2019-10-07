quant_de_testes = int(input())
for c in range(0,quant_de_testes):
  numero = int(input())
  soma = 0
  for c in range(1,numero):
    if numero % c == 0:
      soma += c
  if soma == numero:
    print("{} eh perfeito".format(numero))
  else:
    print("{} nao eh perfeito".format(numero))

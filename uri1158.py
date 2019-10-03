quant_de_testes = int(input())
numeros = []
for c in range(0,quant_de_testes):
    numero = input().split(" ")
    numeros.append(numero)
for c in range(0,len(numeros)):
    primeiro_elemento = int(numeros[c][0])
    quant_de_impares = int(numeros[c][1])
    contador = 0
    soma = 0
    while contador < quant_de_impares:
        if primeiro_elemento % 2 == 0:
            primeiro_elemento += 1
        else:
            soma += primeiro_elemento
            contador += 1
            primeiro_elemento += 2
    print(soma)

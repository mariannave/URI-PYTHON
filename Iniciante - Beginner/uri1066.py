'''
  Entrada: -5
						0
						-3
						-4
						12
  Saída:  3 valor(es) par(es)
					2 valor(es) impar(es)
					1 valor(es) positivo(s)
					3 valor(es) negativo(s)
'''

lista = []

i = 0
while i < 5:
	numero = int(raw_input())
	lista.append(numero)
	i = i +1

i = 0
pares = 0
impares = 0
positivos = 0
negativos = 0
while(i < len(lista)):
	if(lista[i] %2 == 0):
		pares = pares + 1
	elif(lista[i] %2 != 0):
		impares = impares + 1

	if(lista[i] > 0):
		positivos = positivos + 1
	elif(lista[i] < 0):
		negativos = negativos + 1

	i = i +1

print "%d valor(es) par(es)" %pares
print "%d valor(es) impar(es)" %impares
print "%d valor(es) positivo(s)" %positivos
print "%d valor(es) negativo(s)" %negativos

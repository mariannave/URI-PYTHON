'''
  Entrada:  7
						-5
						6
						-4
						12
  Saída:  3 valores pares
'''

n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())
n4 = int(raw_input())
n5 = int(raw_input())

lista =[n1,n2,n3,n4,n5]

i = 0
pares = 0
while(i < len(lista)):
	if(lista[i] %2 == 0):
		pares = pares + 1

	i = i +1


print "%d valores pares" %pares

'''
  Entrada: 8
  Saída:  1
  	3
	5
	7
'''

numero = int(raw_input())
i = 1
while(i <= numero):
	if(i%2 != 0):
		print i
	i = i + 1

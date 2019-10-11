'''
  Entrada:
  Dia 5
  08 : 12 : 23
  Dia 9
  06 : 13 : 23
  Saída:
  3 dia(s)
  22 hora(s)
  1 minuto(s)
  0 segundo(s)
'''

diainicio = raw_input().split()
diainicio = int(diainicio[1])
horainicio = raw_input().split(":")
hinicio = int(horainicio[0])
minicio = int(horainicio[1])
sinicio = int(horainicio[2])

diafinal = raw_input().split()
diafinal = int(diafinal[1])
horafinal = raw_input().split(":")
hfinal = int(horafinal[0])
mfinal = int(horafinal[1])
sfinal = int(horafinal[2])

dia = diafinal - diainicio

hora = hfinal - hinicio
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1

minuto = mfinal - minicio
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1

segundos = sfinal - sinicio
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

print "%d dia(s)" %dia
print "%d hora(s)" %hora
print "%d minuto(s)" %minuto
print "%d segundo(s)" %segundos

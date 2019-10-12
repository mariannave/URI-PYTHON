n=int(input())
b=[]
d=0
for c in range (0,n):
    b.append(input().split(" "))
for c in b:
    print("{:.1f}".format((float(c[0])*2+float(c[1])*3+float(c[2])*5)/10))
    
    
'''
    Entrada: 
3
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0
    Saída: 
5.7
6.3
9.3
 
'''

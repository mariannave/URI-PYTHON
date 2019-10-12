n=int(input())
a=[]
for c in range(0,n):
    a.append(int(input()))
for c in a:
    if c==0:
        print("NULL")
    if c>0 and c%2==0:
        print("EVEN POSITIVE")
    if c>0 and c%2==1:
        print("ODD POSITIVE")
    if c<0 and c%2==0:
        print("EVEN NEGATIVE")
    if c<0 and c%2==1:
        print("ODD NEGATIVE")
        
        '''
    Entrada: 
4
-5
0
3
-4
    Saída: 
ODD NEGATIVE
NULL
ODD POSITIVE
EVEN NEGATIVE
    
'''

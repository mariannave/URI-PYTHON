a=[]
for c in range(0,100):
    a.append(int(input()))
k=max(a,key=int)
print(k)
print(a.index(k)+1)

'''
    Entrada:  
2
113
45
34565
6
...
8
    Saída:
34565
4

'''
        

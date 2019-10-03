a=[]
for c in range(0,100):
    a.append(int(input()))
k=max(a,key=int)
print(k)
print(a.index(k)+1)
        

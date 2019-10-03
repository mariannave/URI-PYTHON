a=[]
a.append(int(input()))
a.append(int(input()))
a.sort(key=int)
soma=0

if a[0]%2==1 and a[1]%2==1:
    while a[0]<a[1]:
        a[0]+=2
        soma+=a[0]
    print(soma-a[1])
if a[0]%2==0 and a[1]%2==0:
    a[0]+=1
    soma+=a[0]
    while a[0]<a[1]:
        a[0]+=2
        soma+=a[0]
    print(soma-(a[1]+1))
if a[0]%2==0 and a[1]%2==1:
    a[0]+=1
    soma+=a[0]
    while a[0]<a[1]:
        a[0]+=2
        soma+=a[0]
    print(soma-a[1])
if a[0]%2==1 and a[1]%2==0:
    while a[0]<a[1]:
        a[0]+=2
        soma+=a[0]
    print(soma-(a[1]+1))

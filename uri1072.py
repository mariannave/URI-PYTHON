n=int(input())
a=[]
inn=0
out=0
for c in range(0,n):
    a.append(int(input()))
for c in a:
    if 10<=c<=20:
        inn+=1
    elif c<10 or c>20:
        out+=1
print("{} in\n{} out".format(inn,out))

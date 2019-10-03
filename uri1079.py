n=int(input())
b=[]
d=0
for c in range (0,n):
    b.append(input().split(" "))
for c in b:
    print("{:.1f}".format((float(c[0])*2+float(c[1])*3+float(c[2])*5)/10))
    

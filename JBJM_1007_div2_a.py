
l=[]
while t>0:
    n=int(input())
    if n%3==1:
        l.append("YES")
    else:
        l.append("NO")
    t=t-1
for i in range(len(l)):
    print(l[i])
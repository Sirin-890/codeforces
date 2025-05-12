t = int(input())
l2=[]
while t>0:
    l=list(map(int,input().split(" ")))
    n=l[0]
    k=l[1]
    p=l[2]
    k=abs(k)
    y = int(k/p)
    if y<n+1:
        if k%p!=0:
            if y+1<=n:
                l2.append(y+1)
            else:
                l2.append(-1)

            
        
            
        else:
            
            l2.append(y)
    else:
        l2.append(-1)
    t=t-1
for i in range(len(l2)):
    print(l2[i])
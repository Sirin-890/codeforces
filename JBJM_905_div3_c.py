t=int(input())
result=[]
while t>0:
    n,k =map(int,input().split())
    lis=list(map(int,input().split()))
    l=[]
    for i in lis:
        if k!=4:
    
            if i%k!=0:
              l.append(i%k)
            else:
              l.append(k)
        else:
           pass
    min_rem= k-max(l)
    result.append(min_rem)
    t=t-1
for r in result:
    print(r)


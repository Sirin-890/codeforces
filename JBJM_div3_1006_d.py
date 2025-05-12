t= int(input())

ans=[]
while t>0:
    l2=[]
    n=int(input())
    l=list(map(int,input().split(" ")))
    for i in range(len(l)):
        count=0
        index=i
        for j in range(len(l)):
            if j>i:
                if l[i]>l[j]:
                    count=count+1
                    index=j
        l2.append([count,index,i])
    max_value = max(l2, key=lambda x: x[0])[0]
    ans.append([i+1,index+1])
    t=t-1

for i in range(len(ans)):
    print(f"{ans[i][0]} {ans[i][1]}")




                    


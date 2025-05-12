t=int(input())
l=[]
while t>0:
    num=int(input())
    a=input()
    n=a.count("-")
    n0=int(n/2)
    n2=a.count("_")
    
    n1=n-n0
    l.append(n2*n1*n0)
    t=t-1
for i in range(len(l)):
    print(l[i])


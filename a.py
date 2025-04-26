a=int(input())
l=[]
s=[]
for i in range(a):
    b=list(map(int,input().split()))
    l.append(b)
for i in range(a):
    s.append(l[i])
    s[0].sort()
    l[i]=s[0]
    s.remove(l[i])
k=set(tuple(i) for i in l)
print(len(k))
l=list(map(int,input().split()))
n=len(l)
a=[]
d=[]
for i in range(1,n+1):
   a.append(i)
for i in a:
   if i not in l:
      d.append(i)
print(d[0])
   
n=int(input())
a=input().split()
for i in range(n):
  a[i]=int(a[i])

d=[]
for i in range(24):
  d.append(0)

for i in range(n):
  d[a[i]]+=1

for i in range(23,0):
  print(d[i], end=' ')

#못품. 정렬 다중 조건 어케하징
n=int(input())
a=[]
for i in range(n):
  name, k, m, e=input().split()
  a.append((name,int(k),int(m),int(e)))

a.sort(reverse=True, key=lambda s:s[1]) #국어점수 감소순
a.sort(key=lambda s:s[2])
a.sort(reverse=True, key=lambda s:s[3])
a.sort(key=lambda s:s[0])

for i in range(n):
  print(a[i])

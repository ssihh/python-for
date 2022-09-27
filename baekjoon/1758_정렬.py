#알바생 강호
n=int(input())
t=[int(input()) for i in range(n)]
t.sort(reverse=True) #내림차순 정렬해주고

sum=0

for i in range(n):
  if t[i]-i >=0:  
    sum+=t[i]-i

print(sum)

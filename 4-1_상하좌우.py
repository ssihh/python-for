n=int(input())
map=[[1]*n for _ in range(n)]

way=list(input().split())

a=0
b=0

for i in way:
  if 0<=a<=(n-1) and 0<=b<=(n-1):
    if i=='L' and b!=0:
      b-=1
    if i=='R' and b!=(n-1):
      b+=1
    if i=='U' and a!=0:
      a-=1
    if i=='D' and a!=(n-1):
      a+=1

print((a+1),(b+1))
# print(map)
# print(way)

'''
5
R R R U D D
'''

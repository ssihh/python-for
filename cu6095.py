# d=[]
# for i in range(20):
#   d.append([])
#   for j in range(20):
#     d[i].append(0)
d = [[0 for j in range(20)] for i in range(20)]

n=int(input())
for i in range(n):
  x,y=input().split()
  d[int(x)][int(y)]=1

for i in range(1,20):
  for j in range(1,20):
    print(d[i][j], end=' ') #공백을 두고 한줄로 출력
  print() #줄바꿈





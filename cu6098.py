c=[]
a,b=input().split()
for i in range(int(a)):
  c.append([])
  for j in range(int(b)):
    c[i].append(0)

n=int(input())
for i in range(n): #n막대의 개수
  l,d,x,y=input().split() #l길이,h방향
  for j in range(int(l)):
    if int(d)==0:
      for i in range(int(l)):
        c[int(x)-1][int(y)-1+i]=1
    else:
      for i in range(int(l)):
        c[int(x)-1+i][int(y)-1]=1
  
for i in range(int(a)):
  for j in range(int(b)):
    print(c[i][j], end=' ') #공백을 두고 한줄로 출력
  print() #줄바꿈


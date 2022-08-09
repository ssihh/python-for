c=[]
for i in range(10):
  c.append([])
  a=input().split()
  for j in range(10):
    c[i].append(int(a[j]))

c[1][1]=9
i=1
j=1
while c[i][j+1]==0 or c[i+1][j]==0:
  if c[i][j]==9: #9인 위치
    if c[i][j+1]==0: #오른쪽 비어있으면9
      j+=1
      c[i][j]=9

    elif c[i][j+1]==1:#오른쪽 막혀있으면
      if c[i+1][j]==0:#아래로 방향틀기
        i+=1
        c[i][j]=9

if c[i][j+1]==2: #오른쪽 2
            j+=1
            c[i][j]=9
if c[i+1][j]==2: #아래쪽 2
          i+=1
          c[i][j]=9

for i in range(10):
  for j in range(10):
    print(c[i][j], end=' ') #공백을 두고 한줄로 출력
  print() #줄바꿈


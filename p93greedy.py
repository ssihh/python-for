n,m,k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

while 1:
  for i in range(k): #k번만 더하기 k<=m
    if m==0: #m더할수 있는 전체 수
      break
      
    result+=first
    m-=1
    
  if m==0:
    break

  result+=second
  m-=1 #가장 큰수를 k버 더하고 두번째로 큰 수를 한번 더하는 연산

print(result)

    

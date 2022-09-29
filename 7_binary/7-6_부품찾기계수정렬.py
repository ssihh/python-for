n=int(input())
array=[0]*1000001

#입력받는거 신기하다. 가은이가 이해시켜줌.
for i in input().split(): #가게에 있는 전체 부품 번호를 입력받아서 기록
  array[int(i)]=1  

m=int(input())
x=list(map(int, input().split()))

for i in x:
  if array[i]==1:
    print('yes', end=' ')
  else:
    print('no', end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''

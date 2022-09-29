n=int(input())
array=set(map(int, input().split())) #집합자료형 set()
# array=list(map(int, input().split())) 리스트 써도되는데 왜 집합자료형 쓰는걸까용

m=int(input())
x=list(map(int,input().split()))

for i in x:
  if i in array: #존재하는지 확인.. 초간단
    print('yes', end=' ')
  else:
    print('no', end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''

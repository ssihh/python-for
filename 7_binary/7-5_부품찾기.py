n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

a.sort()
b.sort()
# print(a,b)
def binary(array, target, start, end):
  if start>end:
    return 'no'
  mid=(start+end)//2 #괄호 안쳐서 안됐엇음 ㅋ
  
  if array[mid]>target:
    return binary(array, target, start, mid-1)
  elif array[mid]<target: #7<9 #8<9
    return binary(array, target, mid+1, end) #3,4 #4,4
  else: #array[mid]==target
    return 'yes'

for i in range(m):
  print(binary(a,b[i],0,n-1),end=' ') #9 

'''
5
8 3 7 9 2
3
5 7 9
'''

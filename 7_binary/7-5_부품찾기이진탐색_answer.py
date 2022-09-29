
def binary_search(array, target, start, end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target:
      return mid #이건 None만 아니면 되서
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1
  return None #None 반환유무에 따라

n=int(input())
array=list(map(int,input().split()))
array.sort()
m=int(input())
x=list(map(int,input().split()))

for i in x: #이렇게 확인하는거
  result=binary_search(array, i, 0, n-1)
  if result!=None:
    print('yes',end=' ')
  else:
    print('no',end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''

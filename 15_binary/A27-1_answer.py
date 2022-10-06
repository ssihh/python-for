#정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array,x):
  a=first(array,x,0,n-1)
  if a==None:
    return -1
  b=last(array,x,0,n-1)
  return b-a+1

#처음위치를 찾는 이진탐색 재귀. 
def first(array, target, start, end):
  if start > end:
    return None
  mid=(start+end)//2
  if (mid==0 or array[mid-1]<target) and array[mid]==target:
    return mid
  elif array[mid]>=target: #타겟보다 크면 왼쪽탐색. 여기는 작거나 같으면인데
    return first(array, target, start, mid-1)
  else: #타겟보다 작으면 오른쪽 탐색
    return first(array, target, mid+1, end)

#마지막 위치를 찾는 이진탐색 재귀
def last(array, target, start, end):
  # if start > end:#없어도 될거같은데
  #   return None
  mid=(start+end)//2
  if (mid==n-1 or array[mid+1]>target) and array[mid]==target:
    return mid
  elif array[mid]>target: #여기는 작으면이네
    return last(array, target, start, mid-1)
  else: #크거나 같으면
    return last(array, target, mid+1, end)

n,x=map(int,input().split())
array=list(map(int, input().split()))
print(count_by_value(array, x)) #x=target 찾는값

'''
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
'''

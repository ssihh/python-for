#이진탐색 재귀. O(logN)
def binary(array, start, end):
  if start > end:
    return -1
  mid=(start+end)//2
  if (mid==array[mid]):
    return mid
  elif array[mid]>mid: # =이 들어가면 안되지
    return binary(array, start, mid-1)
  else: #타겟보다 작으면 오른쪽 탐색
    return binary(array, mid+1, end)

n=int(input())
array=list(map(int, input().split()))
print(binary(array, 0, n-1)) #포문 돌릴 필요없구낭

'''
5
-15 -6 1 3 7
7
-15 -4 2 8 9 13 15
7
-15 -4 3 8 9 13 15
'''

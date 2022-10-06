#시간복잡도 O(logN)으로. 틀린풀이
def binary(array, target, start, end):
  if start > end:
    return -1
  mid=(start+end)//2
  if (mid==array[mid]) and array[mid]==target: #조건이 이상하쥬 
    return mid
  elif array[mid]>=target: #타겟보다 크면 왼쪽탐색. 여기는 작거나 같으면인데
    return binary(array, target, start, mid-1)
  else: #타겟보다 작으면 오른쪽 탐색
    return binary(array, target, mid+1, end)

n=int(input())
array=list(map(int, input().split()))
a=[]
for i in array: #여기서 시간복잡도 N되는거아냐?
  result=binary(array, i,0,n-1)
  a.append(result)
print(max(a))

'''
5
-15 -6 1 3 7
7
-15 -4 2 8 9 13 15
7
-15 -4 3 8 9 13 15
'''

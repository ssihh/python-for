# 퀵정렬 O(NlogN). 호어분할: 첫 번째 데이터를 피벗. 재귀씀!

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:  #원소가 1개면 종료
     return
  pivot = start #피벗은 첫번째원소
  left=start+1
  right=end
  while left<=right: #엇갈렷다면 그만하지롱
    #피벗보다 큰 데이터를 찾을 때까지 반복  
    while left<=end and array[left]<=array[pivot]: #피벗보다 왼족부터 left 큰 데이터를 찾을때까지 반복
      left+=1
    while right>start and array[right]>=array[pivot]: #피벗보다 오른쪽부터 right 작은 데이터를 찾을때까지 반복
      right-=1 
    if left>right: #엇갈렷다면 right 작은 데이터와 pivot 피벗을 교체. 원래 left가 right 보다 왼쪽 작아야함.
      array[pivot], array[right]= array[right], array[pivot]
    else:
      array[left], array[right]= array[right], array[left] #아니면 큰데이터와 작은데이터 교체
  quick_sort(array, start, right-1) #재귀재귀
  quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)

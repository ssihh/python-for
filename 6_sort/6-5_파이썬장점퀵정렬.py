# 파이썬의 장점을 살린 퀸 정렬 소스코드. 전통 퀵 정렬의 분할 방식과는 조금 다름.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  #리스트가 하나 이하의 원소만을 담고 있다면 종료 
  if len(array)<=1:
    return array

  pivot=array[0] 
  tail=array[1:]

  left_side=[x for x in tail if x<=pivot] #분할된 왼쪽 부분에 작은 것들만 
  right_side=[x for x in tail if x>pivot] #분할된 오른쪽 부분 

  #분할이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

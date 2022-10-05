from bisect import bisect_left, bisect_right

def count_by_value(a, left_value, right_value):
  right_index=bisect_right(a,right_value)    
  left_index=bisect_left(a,left_value)
  result=right_index-left_index
  if result==0:
    return -1
  return result

n,x=map(int, input().split())
array=list(map(int, input().split()))

print(count_by_value(array,x,x))

'''
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
'''

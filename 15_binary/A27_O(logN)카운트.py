#O(logN)으로 알고리즘 짜야하는데 2하나 카운트하고 어케해야하징 내가푼건 시간복잡도 고려안한거
n,x=map(int, input().split())
array=list(map(int,input().split()))

result=array.count(x)
if result==0:
  result=-1
print(result)

# start=0
# end=n
# result=0
# while start<=end:
#   mid=(start+end)//2
#   for i in range(n):
#     if array[mid]==x:
#       result+=1
#     elif array[i]
'''
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
'''

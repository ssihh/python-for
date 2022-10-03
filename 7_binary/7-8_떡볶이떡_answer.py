n,m=map(int,input().split())
array=list(map(int, input().split())) #집합자료형 set()

start=0
end=max(array)
result=0

while(start<=end): #같아지거나 작을때까지만
  total=0
  mid=(start+end)//2
  for x in array:
    if x>mid:
      total+=x-mid

  if total<m:  #떡의 양이 부족한 경우 (왼쪽 부분 탐색)
    end=mid-1 #start,end: 15,16 -> 15,14
  else: #떡의 양이 많은 경우 (오른쪽 부분 탐색)
    result=mid
    start=mid+1

print(result)

'''
4 6
19 15 10 17
결과: 15
4 8
19 15 10 17
결과: 14
'''

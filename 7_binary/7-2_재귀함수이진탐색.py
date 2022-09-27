#이진 탐색 소스코드 구현(재귀함수)
def binary_search(array, target, start, end): #array, 7, 0, 9
  if start>end:
    return None
  mid=(start+end)//2 #4. 중간점 의미. 몫연산자//
  if array[mid] == target: #찾은 경우 중간점 인덱스 반환 
    return mid #3
  elif array[mid]>target: #중간값보다 값이 작은 경우 왼쪽확인. 9
    print(start, mid-1)
    return binary_search(array, target, start, mid-1) #a,7,0,3
  else: #중간값크면 오른쪽확인.
    print(mid+1, end)
    return binary_search(array, target, mid+1, end)

n, target=list(map(int, input().split()))
array=list(map(int, input().split()))

result=binary_search(array, target, 0, n-1) 
if result==None:
  print("원소가 존재하지 않습니다.") # 3: a,6,0,3 m1 / 4: a,6,2,3 m2
else:
  print(result+1)

'''
10 7
1 3 5 7 9 11 13 15 17 19
결과: 4
10 7
1 3 5 6 9 11 13 15 17 19
결과: 원소가 존재하지 않습니다.
'''

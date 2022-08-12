n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data: #행의 숫자들 가져다가 비교
      min_value = min(min_value, a)
    result = max(min_value, result)  #max 큰수 뽑기

print(result)
'''
입력예시1
3 3
3 1 2 
4 1 4
2 2 2 
출력예시1: 2

입력예시2
2 4
7 3 1 8 
3 3 3 4
출력예시2: 3
'''

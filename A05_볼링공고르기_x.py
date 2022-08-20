#틀린 풀이 - max 값을 활용안함. 무게가같은 공 3개가 입력되면 틀린 값이 나옴
n, max = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

com = data[0]
result = int((n * (n - 1)) // 2) #조합공식 사용

for i in range(1, n):
    if com == data[i]:
        result -= 1 #같은건 카운트 빼주기
    com = data[i]

print(result)
'''
입력예시:
5 3
1 3 2 3 2
출력: 8
8 5
1 5 4 3 2 4 5 2
출력: 25
4 3
2 2 2 3 
출력: 2
'''

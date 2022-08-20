n, max = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

com = data[0]
result = int((n * (n - 1)) // 2)

for i in range(1, n):
    if com == data[i]:
        result -= 1
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
'''

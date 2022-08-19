n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 1

for i in data:
    if i > result:  #i가 result값보다 클 때 탈출
        break
    result += i

print(result)

'''
5
3 2 1 1 9
출력: 8
3
3 7 8
출력: 1
'''

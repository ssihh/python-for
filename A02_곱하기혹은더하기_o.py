num = str(input())
k = []
result = 0
#str(): 문자열 형태로 바꿔줌
for i in map(int, num):
    k.append(i)
for j in k:
    if result == 0 or result == 1:
        result += j
    else:
        result *= j

print(result)
'''
입력:
02984
출력: 576

입력:
567
출력: 210
'''

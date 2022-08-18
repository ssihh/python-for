#틀린풀이 101034 넣으면 12가 나옴 0일때 곱해버려서
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

입력:
101034
출력: 24
'''

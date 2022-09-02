data = input()
# print(data[1])
num = []
# print(num)
for i in range(len(data)):
    num.append(int(data[i]))
# 위처럼 굳이 새로 배열 만들어서 넣어줄 필요없음
# 바로 int(data[i])로 쓰면됨
h = (int(len(data) / 2))
left, right = 0, 0
for j in range(h):
    left += num[j]
for k in range(-1, -h - 1, -1):
    right += num[k]

if left == right:
    print('LUCKY')
else:
    print('READY')
'''
123402
출력1: LUCKY
7755
출력2: READY
'''

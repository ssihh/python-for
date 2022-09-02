n = input()
lenght = len(n)
summary = 0

for i in range(lenght // 2):
    summary += int(n[i])

for i in range(lenght // 2, lenght):
    summary -= int(n[i])

if summary == 0: #변수 하나만 이용해서 가능
    print('LUCKY')
else:
    print('READY')

'''
123402
출력1: LUCKY
7755
출력2: READY
'''

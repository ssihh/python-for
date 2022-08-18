num = input()
data = []
count = 0
result = 0
#첫 번째 문자를 숫자로 변경하여 대입
for i in range(len(num)):
    data.append(int(num[i]))

for j in range(1, len(num)):
    if num[j - 1] != num[j]:
        count += 1

result += count // 2
result += count % 2

print(result)
'''
입력예시:
0001100
출력: 1
'''

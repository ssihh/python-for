#시간안에 못품. 맞게 출력도 안댐.
n = int(input())
result = 0

for h in range(n):
    if h % 10 == 3 or h // 10 == 3:
        result += 3600
        h += 1
        continue
    h += 1
    for m in range(60):
        if m % 10 == 3 or m // 10 == 3:
            result += 60
            # print(m)
            m += 1
            continue
        m += 1
        for s in range(60):
            if s % 10 == 3 or s // 10 == 3:
                result += 1
                s += 1
                continue
            s += 1
# print(13%10, 31//10)
print(result)

'''
5
11475
'''

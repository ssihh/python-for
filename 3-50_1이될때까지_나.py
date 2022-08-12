n, m = map(int, input().split())

count = 0
while n != 1:
    if n % m == 0:
        n //= m
        count += 1
    else:
        n -= 1
        count += 1
print(count)
'''
입력예시1
25 5
출력예시1: 2

입력예시2
25 3
출력예시2: 6
'''

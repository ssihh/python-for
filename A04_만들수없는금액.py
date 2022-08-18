n = int(input())
data = list(map(int, input().split()))
data.sort()
result=1
a=0
for i in data:
  if result<i:
    break
  result+=i
print(result)

'''
5
3 2 1 1 9
출력예시: 8
'''

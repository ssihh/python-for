n, k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort() #정렬먼저하기
b.sort(reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i], b[i]=b[i],a[i]
  else:
    break #반복문 탈출할 수 있게 해주깅

print(sum(a))

'''
5 3
1 2 5 4 3
5 5 6 6 5
결과: 26
'''

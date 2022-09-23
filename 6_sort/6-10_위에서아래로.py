n=int(input())
array=[int(input()) for _ in range(n)]
array.sort(reverse=True)
for i in array:
  print(i, end=' ')

'''
3
15
27
12
결과: 27 15 12
'''

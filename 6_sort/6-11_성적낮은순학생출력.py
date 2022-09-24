n=int(input())

array=[]
for i in range(n):
  a, b=input().split()
  array.append((a, int(b)))

def setting(data):
  return(data[1])

array.sort(key=setting)

for i in array:
  print(i[0], end=' ')

'''
2
홍길동 95
이순신 77
결과: 이순신 홍길동
'''

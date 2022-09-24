#람다 표현식 사용. 특정한 기능을 수행한느 함수를 한줄에 작성할 수 있다.
n=int(input())

array=[]
for i in range(n):
  input_data=input().split() # 값을 이렇게도 넣을 수 있음
  array.append((input_data[0], int(input_data[1])))

array.sort(key=lambda student: student[1]) #람다 표현식

for i in array:
  print(i[0], end=' ')

'''
2
홍길동 95
이순신 77
결과: 이순신 홍길동
'''

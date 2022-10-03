n,m=map(int,input().split())
array=list(map(int, input().split())) #집합자료형 set()
s=sum(array)//4
result=0

while True:
  
  for i in range(n):
    cut=array[i]-s
    if cut>0:
      result+=cut
      
  if result>=m:
    print(s)
    break
  elif result<m: 
    s-=1
    result=0
    # print('-1하고')

'''
4 6
19 15 10 17
결과: 15
4 8
19 15 10 17
결과: 14
'''

#다이나믹 프로그래밍 방법 중, 메모이제이션(Memoization) 기법 = 캐싱(Caching) 이라고도함.
d=[0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x]=fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))

'''
218922995834555169026
'''

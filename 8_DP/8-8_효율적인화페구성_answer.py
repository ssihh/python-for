# 강의: https://www.youtube.com/watch?v=tWX6FZwwQMI
n,m=map(int, input().split())
array=[int(input()) for _ in range(n)]

d=[10001]*(m+1) #0부터 m원까지

#DP 바텀업
d[0]=0
for i in range(n):
  for j in range(array[i],m+1): #2,8 -> 2~7
    # if d[j-array[i]] !=10001: #(i-k)원을 만드는 방법이 존재하는 경우. 없어도 되는 코드
      d[j]=min(d[j],d[j-array[i]]+1) #d[2]=min(d[2](=10001),d[2-2]+1(=1)) -> 1 
    #0원에서 더해주는 개넘

#계산된 결과 출력
if d[m]==10001:
  print(-1)
else:
  print(d[m])

'''
2 15
2
3
출력: 5

3 4
3
5
7
출력: -1

3 7
2
3
5
출력: 2
'''

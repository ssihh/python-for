#못품 앞의 구현문제 dx,dy 쓰이는 문제였음 우왕
from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]
#print(graph)

def bfs(x,y,n,m,result):
  queue=deque((x,y))
  if graph[x][y]==0: #0이 지나간거
    result+=1

  while queue:
    x,y=queue.popleft()
    result+=1
    #???????????????????

    if x<0 or x>=n or y<0 or y>=m:
      return
    if x==n-1 and y==m-1:
      return result
  
  bfs(x-1,y,n,m,result)
  bfs(x+1,y,n,m)
  bfs(x,y-1,n,m)
  bfs(x,y+1,n,m)

print(bfs(n,m))
# 1,1에서 bfs 써서 +1 씩하고 n,m이면 탈출 break

'''
5 6
101010
111111
000001
111111
111111
'''

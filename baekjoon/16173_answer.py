from collections import deque

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
#print(m)
visited=[[False]*3 for _ in range(n)] #방문목적

dx=[1,0]
dy=[0,1]

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  while queue: #큐가 빌 때까지
    x,y=queue.popleft()
    #visited[x][y]=True
    #print(x,y)
    if graph[x][y]==-1: 
      return 'HaruHaru'
    for i in range(2):
      nx=x+graph[x][y]*dx[i]
      ny=y+graph[x][y]*dy[i]
      if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
       # print('nx,ny저장안함')
        continue
      if visited[nx][ny]==True:
        #print('nx,ny True')
        continue
      if visited[nx][ny]==False:
        visited[nx][ny]=True
        queue.append((nx,ny))

  return 'Hing'

print(bfs(0,0))

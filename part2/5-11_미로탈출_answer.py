from collections import deque

#귿로 따라쳤는데 왜 안되지????

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]
#print(graph)

#상하좌우 구현파트에서 
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque()
  queue.append((x,y)) #튜플 데이터 
  while queue: #큐가 빌 때까지
    x,y=queue.popleft() 
    for i in range(4): #4방향 +1
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue # 공간을 벗어난 경우 무시
      if graph[x][y]==0:
        continue # 벽인 경우 무시
      if graph[nx][ny]==1: # 처음방문하는 경우에만
        graph[nx][ny]=graph[x][y]+1
        graph.append((nx,ny)) #넣어주고
  return graph[n-1][m-1]

print(bfs(0,0))

'''
5 6
101010
111111
000001
111111
111111
'''

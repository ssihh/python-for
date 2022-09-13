from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph=[list(map(int,input())) for _ in range(n)]

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x,y):
  queue=deque()
  queue.append((x,y)) #튜플 데이터 
  while queue: #큐가 빌 때까지
    x, y=queue.popleft() 
    for i in range(4): #4방향 +1
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        #print('공간벗어남')
        continue # 공간을 벗어난 경우 무시
      if graph[nx][ny]==0:
        #print('벽임')
        continue # 벽인 경우 무시
      if graph[nx][ny]==1: # 처음방문하는 경우에만
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny)) #넣어주고
  return graph[n-1][m-1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
'''
5 6
101010
111111
000001
111111
111111
'''


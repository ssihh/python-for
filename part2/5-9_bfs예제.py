from collections import deque

def bfs(graph, start, visited):
  queue=deque([start]) #시작노드
  visited[start]=True
  while queue: #큐가 빌 때까지 반복
    v=queue.popleft() # 빼
    print(v, end=' ') # 1
    for i in graph[v]: # [2,3,8]
      if not visited[i]: #방문하지 않은게 있다면
        queue.append(i)
        visited[i]=True

graph =[
  [], # 0번 비우고
  [2,3,8], # 1번부터 시작
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

bfs(graph, 1, visited)
'''
1 2 3 8 7 4 5 6
'''

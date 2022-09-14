#못품 dfs로 시도함..,.,.
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m, k, x = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph=[list(map(int,input().split())) for _ in range(m)]
#print(graph)

count=0
def dfs(x,y):
  
  for i in range(m):
    a,b=graph[i]

    if a==x: #1부터 출발
      if not visited[i]: #아직 방문안햇다면 방문처리해줌.
        print(a,b,'들림')
        visited[i]=True
        dfs(b,a)


visited=[False]*m #아직 안지나간 거리
print(dfs(x, k)) #시작x가 1이고, 최단거리k가 2인경우

'''
4 4 2 1
1 2
1 3
2 3
2 4
'''


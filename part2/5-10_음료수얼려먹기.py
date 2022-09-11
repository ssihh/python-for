#모르겠음 감이..감이.....
from collections import deque

n,m=map(int, input().split())
graph=[list(map(int,input())) for _ in range(n)]
# 맵을 입력받는 것부터 어렵네 노드로 받는게 편할 거 같은데
  
visited = [[False]*m for _ in range(n)]

#bfs(graph, 1, visited)

print(graph, 0,0,visited)

'''
4 5
00110
00011
11111
00000
'''

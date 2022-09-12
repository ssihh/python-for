n,m=map(int, input().split())
#공백없이 0과 1로 구성된 문자열 형태로 주어지기 때문에
#한줄 입력받고 각 원소를 정수형으로 바꿔서 리스트 형태로 바꾸면
#모든 원소가 0 혹은 1인 정수 리스트가 들어가짐.
graph=[list(map(int,input())) for _ in range(n)]
#print(graph)

# dfs가 한번 쓰이게 되면 해당 노드와 연결된 노드들도 방문처리 할 수 있도록 함
def dfs(x,y): 
  if x<=-1 or x>=n or y<=-1 or y>=m: #주어진 범위를 벗어나는 경우 즉시 종료
    return False
  if graph[x][y]==0: #현재 노드를 아직 방문하지 않았다면 
    graph[x][y]=1 #해당노드 방문처리
    dfs(x-1,y) #상하좌우 재귀적. 리턴값 사용X. 
    dfs(x+1,y) #연결된 모든 노드에 대해서 방문처리를 수행하기 위한 목적으로 수행
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

result =0 #아이스크림 개수
for i in  range(n):
  for j in range(m): #n*m 각 위치에서 dfs 수행
    if dfs(i,j)==True: # 방문처리가 된거라면 +1. 즉, 처음 방문하는 것이라면 +1
      result+=1 

print(result)

'''
4 5
00110
00011
11111
00000
[[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

3
'''

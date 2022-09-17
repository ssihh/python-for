#런타임에러
n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
#print(m)
check=[]

def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return False
  if graph[x][y]==-1: #이거없으면 안됨 왜안되지
    #print('HaruHaru')
    check.append(graph[x][y])
    return True
  move=graph[x][y]
  #print(move)
  dfs(x+move,y)
  dfs(x,y+move)
  #print('Hing')
  check.append(graph[x][y])
  return False

dfs(0,0)
# print(check)
if -1 in check:
  print('HaruHaru')
else:
  print('Hing')

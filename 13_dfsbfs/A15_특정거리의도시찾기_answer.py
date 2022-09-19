from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)] #0비우고 1번부터 시작하기위해

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) #1부터 들어가겠죠???

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1) # -1 -> 방문 여부도 계산하기 위함.
# 최단거리 계산할 리스트 정의(x 값이 도시번호를 의미)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x]) #x=1. deque는 ([])안에 데이터를 저장 int 안됨.
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]: #2, 3
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1 # [2]=0+1 
            q.append(next_node) #apeedn(2)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
'''
4 4 2 1
1 2
1 3
2 3
2 4
'''

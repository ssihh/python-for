# 행이 3개인 2차원 리스트로 인접리스트 표현
graph=[[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1
graph[1].append((0,7))

#노드 2
graph[2].append((0,5))

print(graph)
'''
[[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
'''

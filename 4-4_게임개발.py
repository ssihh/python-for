n, m = map(int, input().split())
a, b, direct = map(int, input().split())
#2차원 리스트 입력받는 법 외우기
map = [list(map(int,input().split())) for _ in range(n)] 
#북 동 남 서
d=[0,1,2,3]
dx=[0,1,0,-1]
dy=[-1,0,1,0]

index(direct) #index()안에 있는 값을 찾아 해당 위치를 반환
#왼쪽으로 도는거 부터 막힘.. 북쪽기준 0 3 2 1 이렇게 돌아야하는데
for dir in range(len(d),-1,-1):
    
print(map)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

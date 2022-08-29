n, m = map(int, input().split())
#방문할 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1  #현재좌표 방문 처리

#2차원 리스트 입력받는 법 외우기
array = [list(map(int, input().split())) for _ in range(n)]

#북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


#왼쪽으로 회전
def turn_left():
    global direction #함수 바깥에서 선전된 전역변수
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while 1:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction] #direction 순서에 따라 북동남서
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않을 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue 
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 없다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

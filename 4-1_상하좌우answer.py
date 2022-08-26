#N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1] #x좌표 +0
dy = [-1, 1, 0, 0] #y좌표 +1 일 때,
move_types = ['L', 'R', 'U', 'D'] #L로 이동한다.

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]: #R일때
            nx = x + dx[i] #nx = 1 + 0
            ny = y + dy[i] #ny = 1 + 1
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue #반복문의 처음으로 돌아간다
    #벗어나지 않는다면 이동 수행
    x, y = nx, ny #따로 초기화를 하는이유는 벗어나는 경우 거를라고 필터링하려궁~

print(x, y)

'''
5
R R R U D D
'''

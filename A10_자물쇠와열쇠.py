#못풀었음.
def solution(key, lock):
    answer = True

    for i in range(3):
        for j in range(3):
            if key[i][j] + lock[i][j] == 2:
                continue
            else:
                answer = False  #정방향에서 안맞으면 false

# key전체합과 lock전체합이 서로 다르면 좌측 우측으로 움직여야함.
# 회전 구현은
# key[0][0]=key[2][0]
# key[0][1]=key[1][0]
# key[0][2]=key[0][0]

# key[1][0]=key[2][1]
# key[1][1]
# key[1][2]

    for i in range(len(key)): #시계방향으로 90도 회전
      key[i][0]=key[2][i]
      key[i][1]=key[1][i]
      key[i][2]=key[0][i]

    return answer

key = [[0, 0, 0], 
       [1, 0, 0], 
       [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(len(key))
print(solution(key, lock))

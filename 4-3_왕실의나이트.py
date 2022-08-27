l = list(input())
x = int(l[1])
y = ord(l[0])  #a 열
# print(ord(l[0]))
result = 0
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 1, -1, -2, -1]  #열

for i in range(8):  #1way가 1일때
    nx, ny = 0, 0
    nx = x + dx[i]
    ny = y + dy[i]
    #print(nx, ny)
    if nx < 1 or nx > 8 or ny < ord('a') or ny > ord('h'):
        continue
    result += 1
print(result)
'''
a1
2
'''

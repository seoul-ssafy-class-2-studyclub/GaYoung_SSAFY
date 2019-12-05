'''
3 3
1 1 0
1 1 1
1 0 1
1 1 1

5 5
2 3 0
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
'''



N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
x, y, d = r, c, d
stop = False
flag = True
while True:

    if stop:
        break
    if flag:
        board[x][y] = 2
        cnt += 1
    flag = False
    for i in range(4):
        dd = (d + 3 - i) % 4
        xi, yi = x + dx[dd], y + dy[dd]
        if board[xi][yi] == 0:
            flag = True
            break

    if flag:  # 왼쪽확인 경우
        x, y, d = xi, yi, dd
        continue
    else:  # flag == False

        xx, yy = x - dx[d], y - dy[d]
        if board[xx][yy] == 1:  # d
            stop = True

        else:
            x, y, d = xx, yy, d

print(cnt)

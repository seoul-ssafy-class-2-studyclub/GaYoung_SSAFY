'''
4 4
####
#JF#
#..#
#..#

4 4
####
#J.#
#.F#
#..#
'''

from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
jihun = deque()
fire = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            jihun.append((i, j))
        elif board[i][j] == 'F':
            fire.append((i, j))

flag = False
# flag = True가 되면 cnt값 print하기 => flag=True이면 break
cnt = 0
while jihun:
    cnt += 1
    for i in range(len(jihun)):
        x, y = jihun.popleft()
        # jihun이 돌고 fire가 돌아서 J자리가 F가 된다면, 그냥 pass
        # 불이 지훈자리에 가면 지훈deque에 있는 것을 삭제해야함 -> 삭제보다는 나오면 돌리지 않는 것이 굳
        if board[x][y] == 'F':
            continue
        else:
            for a, b in near:
                xi, yi = x + a, y + b
                if 0 <= xi < R and 0 <= yi < C:
                    if board[xi][yi] == '.':
                        board[xi][yi] = 'J'
                        jihun.append((xi, yi))

                else:
                    flag = True
                    break
    if flag:
        break

    for i in range(len(fire)):
        x, y = fire.popleft()
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < R and 0 <= yi < C:
                if board[xi][yi] == '.' or board[xi][yi] == 'J':
                    board[xi][yi] = 'F'
                    fire.append((xi, yi))

if flag:
    print(cnt)
else:
    print('IMPOSSIBLE')

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


fire_flag = False
jihun_flag = False
cnt = 0
while jihun:
    for i in range(len(jihun)):
        x, y = jihun.popleft()
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < R and 0 <= yi < C:
                if board[xi][yi] == '.':
                    board[xi][yi] = 'J'
                    board[x][y] = '.'
                    cnt += 1
                    jihun.append((xi, yi))
        else:
            jihun_flag = True

    if jihun_flag:
        print('IMPOSSIBLE')
        break


    for i in range(len(fire)):
        x, y = fire.popleft()
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < R and 0 <= yi < C:
                if board[xi][yi] == '.':
                    board[xi][yi] = 'F'
                    fire.append((xi, yi))
                elif board[xi][yi] == 'J':
                    fire_flag = True

    if fire_flag:
        print('IMPOSSIBLE')
        break


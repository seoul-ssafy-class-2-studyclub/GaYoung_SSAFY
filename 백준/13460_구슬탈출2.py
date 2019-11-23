from collections import deque
from pprint import pprint

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def move(x, y, dx, dy):
    while board[x + dx][y + dy] != 0 and board[x + dx][y + dy] != '#':
        x += dx
        y += dy
        # cnt += 1
    return x, y


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
q = deque()
O = []

for i in range(1, N):
    for j in range(1, M):
        b_x, b_y, r_x, r_y = [0] * 4
        if board[i][j] == 'B':
            b_x, b_y = i, j
        elif board[i][j] == 'R':
            r_x, r_y = i, j
        q.append((b_x, b_y, r_x, r_y))
        break


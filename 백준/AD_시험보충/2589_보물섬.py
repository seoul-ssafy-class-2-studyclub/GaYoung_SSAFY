'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''

from collections import deque

near = [(-1, 0), (0, 1), (0, -1), (1, 0)]
def bfs():
    global cnt
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for a, b in near:
                xi, yi = x + a, y + b
                if 0 <= xi < N and 0 <= yi < M and board_[xi][yi] == 'L':
                    board_[xi][yi] = 0
                    q.append((xi, yi))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
mymax = 0
q = deque()
for i in range(N):
    for j in range(M):
        board_ = [row[:] for row in board]
        if board[i][j] == 'L':
            q.append((i, j))
            cnt = -1
            board_[i][j] = 0
            bfs()

            if mymax < cnt:
                mymax = cnt
print(mymax)
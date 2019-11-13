from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q
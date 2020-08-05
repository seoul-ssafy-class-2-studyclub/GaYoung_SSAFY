'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''

from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(a, b):
    q = deque([(a, b)])
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visit = [[0 for _ in range(M)] for _ in range(M)]

    while q:
        x, y = q.popleft()




for i in range(M):
    for j in range(N):
        if board[i][j] > 0:
            q.append((i, j))


cnt = 1
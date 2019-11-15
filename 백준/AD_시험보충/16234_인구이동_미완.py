from collections import deque
from pprint import pprint

def bfs():
    while q:
        x, y = q.popleft()
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < N and visit[xi][yi] == False:
                if L <= abs(board[xi][yi] - board[x][y]) <= R:
                    visit[xi][yi] = True
                    ls.append((xi, yi, board[xi][yi]))
                    q.append((xi, yi))



N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visit = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        ls = deque()
        q = deque()
        if board[i][j] != 0 and visit[i][j] == False:
            q.append((i, j))
            ls.append((i, j, board[i][j]))
            visit[i][j] = True
            bfs()


            # pprint(visit)
            # print(ls)

            if len(ls) != 0:
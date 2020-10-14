from collections import deque

N, L, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

near = [(0, 1),(0, -1),(1, 0),(-1, 0)]
def bfs():
    visit = [[0] * N for _ in range(N)]
    q = deque([])

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                q.append([i, j, board[i][j]])
                visit[i][j] = 1

                while q:
                    x, y, val = q.popleft()

                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < N and 0 <= yi < N and visit[xi][yi] == 0:
                            if L <= abs(board[x][y] - board[xi][yi]) <= R:
                                q.append([xi, yi, board[xi][yi]])
                                visit[xi][yi] = 1


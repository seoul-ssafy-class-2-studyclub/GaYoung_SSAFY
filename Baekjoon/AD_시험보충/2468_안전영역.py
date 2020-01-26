from collections import deque

near = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs():
    while q:
        x, y = q.popleft()
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < N:
                if zone[xi][yi] == 1:
                    q.append((xi, yi))
                    zone[xi][yi] = 0
    return 1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
q = deque()


mymax_h = 0
for i in range(N):
    for j in range(N):
        if mymax_h < board[i][j]:
            mymax_h = board[i][j]

mymax = 0
for m in range(mymax_h):
    zone = [row[:] for row in board]
    for i in range(N):
        for j in range(N):
            if zone[i][j] > m:
                zone[i][j] = 1
            else:
                zone[i][j] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if zone[i][j] == 1:
                q.append((i, j))
                zone[i][j] = 0
                cnt += bfs()

    if mymax < cnt:
        mymax = cnt

print(mymax)





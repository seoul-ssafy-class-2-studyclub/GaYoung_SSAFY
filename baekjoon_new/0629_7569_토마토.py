import collections

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
near = [(0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

q = collections.deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append([i, j, k, 0])

while q:
    x, y, z, cnt = q.popleft()
    for a, b, c in near:
        xi, yi, zi = x + a, y + b, z + c
        if 0 <= xi < H and 0 <= yi < N and 0 <= zi < M:
            if board[xi][yi][zi] == 0:
                board[xi][yi][zi] = 1
                q.append([xi, yi, zi, cnt+1])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                cnt = -1

print(cnt)

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(0, -1), (0, 1), (1, 0)]
visit = [[False] * M for _ in range(N)]


q = deque([1, 1])
while True:
    x, y = q.popleft()

    if x == N and y == N:
        break

    for a, b in near:
        xi, yi = x + a, y + b
        if 0 < xi < N and 0 < yi < M:
            if not visit[xi][yi]:
                q.append((xi, yi))

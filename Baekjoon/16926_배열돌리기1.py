N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = min(N, M) // 2
near = [(1, 0), (0, 1), (-1, 0), (0. -1)]  # 아래, 오른, 위, 왼

for t in range(time):
    temp = board[t][t]
    x, y = t, t

    for a, b in near:
        while 0 <= x < N and 0 <= y < M:
            x += a
            y += b

            temp, board[x][y] = board[x][y], temp


        x -= a
        y -= b

print(board)

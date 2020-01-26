N, M, x, y, K = map(int ,input().split())
board = [list(map(int, input().split())) for _ in range(N)]

go = list(map(int, input().split()))

near = [(0, 1), (0, -1), (-1, 0), (0, 1)]
for g in go:
    xi, yi = x + near[g - 1][0], y + near[g - 1][1]
    if 0 <= xi <= N and 0 <= yi < M:
        x, y = xi, yi
        if board[xi][yi] == 0:
            pass

    else:
        pass


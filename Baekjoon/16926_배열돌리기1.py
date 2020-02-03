N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for r in range(R):
    # 한번 회전하겠다.
    bd = [[0] * N for _ in range(M)]

    for n in range(N // 2 + 1):
        nn, mm = N - 1, M - 1
        # 오른쪽
        for k in range(n, mm - n):
            bd[nn - n][k + 1] = board[nn - n][k]
        # 아래
        for k in range(mm - n, n, -1):
            bd[k][n] = board[k - 1][n]
        # 왼쪽
        for k in range(1 + n, mm - n + 1):
            bd[n][k - 1] = board[n][k]
        # 위
        for k in range(1 + n, mm - n + 1):
            bd[k - 1][nn - n] = board[k][nn - n]

    board = bd

for bb in bd:
    print(' '.join(map(str, bb)))

for t in range(int(input())):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    cnt = 0
    for m in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if board[x][y] == 0:
                    board[x][y] = 1
                    cnt += 1

    print('#{} {}'.format(t+1, cnt))

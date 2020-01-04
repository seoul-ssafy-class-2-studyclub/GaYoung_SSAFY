N = int(input())
board = [list(input()) for _ in range(N)]

bbb = []
eee = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            bbb.append((i, j))
        elif board[i][j] == 'E':
            eee.append((i, j))

visit = [[0] * N for _ in range(N)]


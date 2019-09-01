from pprint import pprint

N, M = map(int, input().split())  # N = col, M = row
board = []
for n in range(N):
    board.append(list(map(int, input().split())))

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            for a, b in d:
                ii = i + a
                jj = j + b
                if 0 <= ii < N and 0 <= jj < M and board[ii][jj] == 0:
                    board[ii][jj] = -1

pprint(board)

N, K = map(int, input().split())

inf = float('inf')
board = [[inf] * (N+1) for _ in range(N+1)]

for k in range(K):
    n1, n2 = map(int, input().split())
    board[n1][n2] = 1

# print(board)
for k in range(N+1):
    for i in range(N+1):
        if i != k:
            for j in range(N+1):
                if j != i and j != k:
                    board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(int(input())):
    n1, n2 = map(int, input().split())
    if board[n1][n2] != inf:
        print(-1)
    elif board[n2][n1] != inf:
        print(1)
    else:
        print(0)

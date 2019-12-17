N, K = map(int, input().split())

board = [[0] * (N+1) for _ in range(N+1)]

for k in range(K):
    n1, n2 = map(int, input().split())
    board[n1][n2] = -1
    board[n2][n1] = 1

for k in range(N+1):
    for i in range(N+1):
        if i != k:
            for j in range(N+1):
                if i != j and j != k:
                    if board[i][k] != 0 and board[i][k] == board[k][j]:
                        board[i][j] = board[i][k]
                        board[j][i] = -board[i][k]

for i in range(int(input())):
    n1, n2 = map(int, input().split())
    print(board[n1][n2])

'''
a -> c : -1
c -> b : -1
결과: a -> b: -1
'''
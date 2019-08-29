def func():
    near = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for [dx, dy] in near:

N, M = map(int,input().split())
board = []

for n in range(N):
    data = list(map(int,input().split()))
    board.append(data)

for n in range(N):
    for m in range(M):
        while True:
            cnt = 0
            if board[n][m] != 0:
                

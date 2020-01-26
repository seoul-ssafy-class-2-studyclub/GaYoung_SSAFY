N = int(input()) 
board = [[0] * 100 for _ in range(100)]
for n in range(N):
    row, col = map(int, input().split())

    for x in range(row, row + 10):
        for y in range(col, col + 10):
            board[x][y] += 1

cnt = 0
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] >= 1:
            cnt += 1

print(cnt)
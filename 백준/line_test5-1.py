n, m = map(int, input())
a, b = map(int, input())

board = [[0] * (a + 1) for _ in range(b + 1)]
board[0][0] = 2
board[b][a] = 3
print(board)  # [[1, 0, 0], [0, 0, 2]]

cnt = 0
for i in range(b + 1):  # 세로
    for j in range(a + 1):  # 가로
        if j == 0 or i == 0:
            cnt = 0
        else:
            cnt = i + j



from pprint import pprint

N = int(input())

board = [[0] * N for _ in range(N)]

number = 1
row = 0
col = N
while col > 0:
    for i in range(row, col):
        board[row][i] = number
        number += 1
    for i in range(row + 1, col):
        board[i][col - 1] = number
        number += 1
    for i in range(col - 2, row - 1, -1):
        board[col - 1][i] = number
        number += 1
    for i in range(col - 2, row, -1):
        board[i][row] = number
        number += 1
    row += 1
    col -= 1
pprint(board)

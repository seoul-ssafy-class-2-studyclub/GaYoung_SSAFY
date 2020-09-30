def solution(n):
    answer = []
    return answer

n = 6
board = [[0] * n for _ in range(n)]
x, y, number = -1, 0, 1
for i in range(n):
    for j in range(i, n):
        if i % 3 == 0:
            x += 1
            print('0')
            print(board)

        elif i % 3 == 1:
            y += 1
            print('1')
            print(board)

        elif i % 3 == 2:
            x -= 1
            y -= 1
            print('2')
            print(board)

        board[x][y] = number
        number += 1

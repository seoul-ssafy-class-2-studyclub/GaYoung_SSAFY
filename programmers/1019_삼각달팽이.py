n = 6

def solution(n):
    board = [[0] * n for _ in range(n)]

    x, y = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # down
                x += 1

            elif i % 3 == 1:  # right
                y += 1

            elif i % 3 == 2:  # up
                x -= 1
                y -= 1

            board[x][y] = number
            number += 1
    # print(board)

    answer = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                answer.append(board[i][j])

    return answer
[[1, 0, 0, 0, 0, 0],
 [2, 15, 0, 0, 0, 0],
 [3, 16, 14, 0, 0, 0],
 [4, 17, 21, 13, 0, 0],
 [5, 18, 19, 20, 12, 0],
 [6, 7, 8, 9, 10, 11]]

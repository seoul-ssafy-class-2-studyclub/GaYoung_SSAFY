def solution(n):
    board = []
    for i in range(1, n + 1):
        board.append([0] * i)

    num = 1
    row = n
    col = 0

    while True:
        if num == n * (n + 1) // 2 + 1:
            break

        for i in range(col, col + row):
            if board[i][col] == 0:
                board[i][col] = num
                num += 1

        for i in range(col + 1, col + row):
            if board[row + col - 1][i] == 0:
                board[row + col - 1][i] = num
                num += 1

        for i in range(row + col - 1, -1, -1):
            for j in range(row + col - 1):
                print(i, j)
                if board[i][j] == 0:
                    board[i][j] = num
                    num += 1
                    break
        print(board)

        row -= 2
        col += 1


    answer = []
    for i in board:
        for j in range(len(i)):
            answer.append(i[j])

    # print(answer)
    return answer

# n = 4
# n = 5
n = 11
print(solution(n))

[[1],
 [2, 30],
 [3, 29, 45],
 [4, 31, 28, 56],
 [5, 32, 46, 27, 63],
 [6, 33, 47, 57, 26, 66],
 [7, 34, 48, 58, 64, 25, 65],
 [8, 35, 49, 59, 60, 61, 24, 62],
 [9, 36, 50, 51, 52, 53, 54, 23, 55],
 [10, 37, 38, 39, 40, 41, 42, 43, 22, 44],
 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21()]]

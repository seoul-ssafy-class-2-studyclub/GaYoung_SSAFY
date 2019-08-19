for case in range(1, 11):
    board = []
    N = int(input())
    for row in range(100):
        board.append(list(map(int, input().split())))
    j = board[99].index(2)
    for i in range(99, 0, -1):
        if j != 0 and board[i][j-1]:
            while j > 0 and board[i][j-1]:
                j -= 1
        elif j != 99 and board[i][j+1]:
            while j < 99 and board[i][j+1]:
                j += 1

    print(f'#{case} {j}')
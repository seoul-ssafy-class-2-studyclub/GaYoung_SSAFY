for t in range(int(input())):
    N = int(input())
    if 1 <= N <= 10:
        board = [[0] * N for _ in range(N)]
    
    value = 1
    row = N
    col = 0
    while row > 0:
        for i in range(col, col + row):
            board[col][i] = value
            value += 1

        for i in range(col + 1, col + row):
            board[i][row + col - 1] = value
            value += 1
        
        for i in range(row + col - 2, col - 1, -1):
            board[row + col - 1][i] = value
            value += 1
        
        for i in range(row + col - 2, col, -1):
            board[i][col] = value
            value += 1
        
        row -= 2
        col += 1

    print('#{}'.format(t + 1))
    for b in board:
        print(' '.join(str(k) for k in b))
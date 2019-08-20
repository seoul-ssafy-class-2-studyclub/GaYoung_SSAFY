for t in range(10):
    board = []
    N = int(input())
    for i in range(100):
        board.append(list(map(int, input().split())))

    start = board[99].index(2)  # 9

    for k in range(99, 0, -1):
        if start != 0 and board[k][start - 1] == 1:
            while start > 0 and board[k][start - 1] == 1:
                start -= 1

        elif start != 99 and board[k][start + 1] == 1:
            while start < 99 and board[k][start + 1] == 1:
                start += 1
    
    print('#{} {}'.format(N, start))
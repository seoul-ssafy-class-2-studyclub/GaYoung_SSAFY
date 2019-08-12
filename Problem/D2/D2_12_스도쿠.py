for t in range(int(input())):
    board = []
    count = 0
    for i in range(9):
        board.append(list(map(int, input().split())))    
    board_re = list(zip(*board))

    # 가로
    for j in board:
        if len(set(j)) != 9:
            count += 1

    # 3 * 3
    point = []
    for k in [0, 3, 6]:
        for l in [0, 3, 6]:
            point.append((k, l))
    for y, x in point:
        test = []
        for n in [0, 1, 2]:
            for m in [0, 1, 2]:
                test.append(board[y + n][x + m])
        if len(set(test)) != 9:
            count += 1
    
    # 세로
    for j in board_re:
        if len(set(j)) != 9:
            count += 1
        
    if count != 0:
        result = 0
    elif count == 0:
        result = 1

    print('#{0} {1}'.format(t+1, result))
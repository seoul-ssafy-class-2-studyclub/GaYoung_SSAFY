board = []
for t in range(int(input())):
    for i in range(9):
        board.append(list(map(int, input().split())))
    # print(board)

    for j in board:
        j_set = set(j)
        if len(j_set) == 9:
            count = 1
        else:
            count = 0
    print(count)

    sum_board = []
    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            sum_board += [board[k][l], board[k][l+1], board[k][l+2]]
            break
    sum_board_set = set(sum_board)
    if len(sum_board_set) == 9:
        count = 1
    else:
        count = 0
    print('#{0} {1}'.format(t+1, count))
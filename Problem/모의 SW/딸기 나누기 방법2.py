for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    result = 0
    for x in range(1, N):
        if result == 1:
            break
        for y in range(1, N):
            if result == 1:
                break
            sum_list = [0, 0, 0, 0]
            for i in range(x):
                sum_list[0] += sum(board[i][0:y])
                sum_list[1] += sum(board[i][y:N])
            for j in range(x, N):
                sum_list[2] += sum(board[j][0:y])
                sum_list[3] += sum(board[j][y:N])
            if sum_list[0] == sum_list[1] == sum_list[2] == sum_list[3]:
                result = 1

    print('#{} {}'.format(t+1, result))
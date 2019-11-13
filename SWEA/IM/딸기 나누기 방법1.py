for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    total_s = 0
    for i in range(N):
        for j in range(N):
            total_s += board[i][j]

    row_s = total_s // 2

    # 가로
    line_r = 0
    sum_r = []
    for x in range(N):
        if line_r == 1 or sum(sum_r) > row_s:  # row_s보다 큰 경우 더이상 계산할 필요없음 -> break 걸어주기
            break
        sum_r += board[x]
        if sum(sum_r) == row_s:
            line_r = 1

    # 세로
    line_c = 0
    sum_c = []
    for x in range(N):
        if line_c == 1 or sum(sum_c) > row_s:  # row_s보다 큰 경우 더이상 계산할 필요없음 -> break 걸어주기
            break
        for y in range(N):
            if line_c == 1 or sum(sum_c) > row_s:  # row_s보다 큰 경우 더이상 계산할 필요없음 -> break 걸어주기
                break
            for i in range(N):
                sum_c += [board[i][y]]
                print(sum_c)
                if sum(sum_c) == row_s:
                    line_c = 1

    result = 0
    if line_r == 1 and line_c == 1:
        result = 1

    print('#{} {}'.format(t+1, result))
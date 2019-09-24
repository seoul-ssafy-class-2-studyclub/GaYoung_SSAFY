for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    stack = []
    near = [(0, 1), (1, 0)]
    result = []

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                x_list = []
                y_list = []
                stack.append(i)
                stack.append(j)
                x_cnt = 1
                y_cnt = 1
                x_list.append(i)
                y_list.append(j)
                while stack:
                    y = stack.pop()
                    x = stack.pop()
                    for a, b in near:
                        xi = x + a
                        yi = y + b
                        if 0 <= xi < N and 0 <= yi < N:
                            if board[xi][yi] != 0:
                                stack.append(xi)
                                stack.append(yi)
                                board[xi][yi] = 0
                                if xi not in x_list:
                                    x_cnt += 1
                                    x_list.append(xi)
                                elif yi not in y_list:
                                    y_cnt += 1
                                    y_list.append(yi)
                result += [[x_cnt * y_cnt, x_cnt, y_cnt]]
    result.sort()
    result.sort()
    print('#{} {}'.format(t+1, len(result)), end=' ')
    answer = []
    for i in range(len(result)):
        answer += [result[i][1], result[i][2]]
    for a in answer:
        print(a, end=' ')
    print()
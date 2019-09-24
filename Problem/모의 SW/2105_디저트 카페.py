for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))
    visit = [False] * 101

    result = -1
    near = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    stack = []
    num_list = []
    for i in range(1, N - 1):
        for j in range(N):
            if board[i][j] != 0:
                stack.append(i)
                stack.append(j)
                num_list.append(board[i][j])
                visit[board[i][j]] = True
                while stack:
                    x = stack.pop()
                    y = stack.pop()
                    for a, b in near:
                        xi = x + a
                        yi = y + b
                        if 0 <= xi < N and 0 <= yi < N and board[xi][yi] not in num_list:
                            stack.append(xi)
                            stack.append(yi)
                            num_list.append(board[xi][yi])
                            if len(num_list) >= 4:
                                ff_num.append(num_list)
            print(num_list)
            print(ff_num)
            print(queue)

# # #     if len(max(final_queue)) == len(num_list):
# # #         result = len(num_list)
# # # # print(queue)
# # # #                                 print(num_list_t)
# # #             print(num_list)
# # # print(result)
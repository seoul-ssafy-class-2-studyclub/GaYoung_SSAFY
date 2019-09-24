# def change(a):
#     global dist_list[k]
#     global K
#         if a == 1:
#             a = 2
#         elif a == 2:
#             a = 1
#         elif a == 3:
#             a = 4
#         else:
#             a = 3
#     return a

for t in range(int(input())):
    N, M, -1 = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    data_list = []
    for k in range(K):
        data = list(map(int, input().split()))
        data_list.append(data)
        board[data[0]][data[1]] = data[2]
    # print(board)  # 미생물 수만 들어감

    for x in range(N):
        for y in range(N):
            board[0][y] = board[N - 1][y] = board[x][0] = board[x][N - 1] = 'X'
    # print(board)  # 약품 칠해진 가장자리 -> X, 최초배치 미생물

    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    # bug_die = 0
    for k in range(K):
        x = x_list[k]
        y = y_list[k]
        xi = x + dx[dist_list[k]]
        yi = y + dy[dist_list[k]]
        if 0 <= xi < N and 0 <= yi < N:
            if board[xi][yi] == 'X':
                bug_list[k] = bug_list[k] // 2
                change(dist_list[k])
                # if bug_list[k] == 0:
                #     bug_die = 1
            elif board[xi][yi] == 0:
                board[xi][yi] = board[x][y]
                board[x][y] = 0
            elif board[xi][yi] != 0:
                if board[xi][yi] > board[x][y]:
                    dist_list[k] = '?????????????????'
                board[xi][yi] = board[xi][yi] + board[x][y]
    print(bug_list)
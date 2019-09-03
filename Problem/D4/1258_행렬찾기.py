<<<<<<< HEAD
def sq(adj):
    square = (adj[2] - adj[0] + 1) * (adj[3] - adj[1] + 1)
    return square

=======
>>>>>>> 31d4b1f6e75258ba6a3e31e43d64dfb2195edcb0
for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

<<<<<<< HEAD
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
=======
    stack = []
    near = [(0, 1), (1, 0)]
    result = []
>>>>>>> 31d4b1f6e75258ba6a3e31e43d64dfb2195edcb0

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
<<<<<<< HEAD
                board[i][j] = 1

    point_t = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board[i][j] = 2
                queue = []
                point = []
                queue.append(i)
                queue.append(j)
                point.append(i)
                point.append(j)
                while queue:
                    x = queue.pop(0)
                    y = queue.pop(0)
                    for idx in range(4):
                        xi = x + dx[idx]
                        yi = y + dy[idx]
                        if 0 <= xi < N and 0 <= yi < N:
                            if board[xi][yi] == 1:
                                board[xi][yi] = 2
                                queue.append(xi)
                                queue.append(yi)
                point.append(x)
                point.append(y)
                point_t.append(point)
    # print(point_t)  # [[0, 0, 0, 1], [2, 0, 3, 2]]
    mymax = 0
    for i in point_t:
        if mymax < sq(i):
            mymax = sq(i)


    print('#{} {}'.format(t, len(point_t)))
=======
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
>>>>>>> 31d4b1f6e75258ba6a3e31e43d64dfb2195edcb0

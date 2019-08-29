def sq(adj):
    square = (adj[2] - adj[0] + 1) * (adj[3] - adj[1] + 1)
    return square

for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
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

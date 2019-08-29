for t in range(int(input())):
    board = []
    N = int(input())
    for n in range(N):
        board.append(list(map(int, input())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = []
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                queue.append([i, j])

    result = 0
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        visit[x][y] = True
        # cnt += 1
        for idx in range(4):
            xi = x + dx[idx]
            yi = y + dy[idx]
            if 0 <= xi < N and 0 <= yi < N and not visit:
                if board[xi][yi] == 0:
                    queue.append([xi, yi])
                    board[xi][yi] = 1
                elif board[xi][yi] == 3:
                    result = 1
                    # if result != 0:
                        # result = cnt
    print(result)
    # print('#{} {}'.format(t+1, result))
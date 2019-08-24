for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        data = list(map(int, input().split()))
        board.append(data)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    island = []
    for row in range(N):
        for col in range(N):
            if board[row][col] != 0:
                for i in range(len(dx)):
                    if board[row + dx[i]][col + dy[i]] != 0:
                        cnt += board[row + dx[i]][col + dy[i]]
                    else:
                        break
    island.append(cnt)
    
    print('#{} {}'.format(t+1, island))

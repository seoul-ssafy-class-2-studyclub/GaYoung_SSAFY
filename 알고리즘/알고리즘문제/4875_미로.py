for t in range(int(input())):
    board = []
    N = int(input())
    for n in range(N):
        board.append(list(map(int, input())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                stack.append([i, j]) 
    result = 0
    while stack:
        x, y = stack.pop()
        for idx in range(4):
            xi = x + dx[idx]
            yi = y + dy[idx]
            if 0 <= xi < N and 0 <= yi < N:
                if board[xi][yi] == 0:
                    stack.append([xi, yi])
                    board[xi][yi] = 1
                elif board[xi][yi] == 3:
                    result = 1
                    stack = []
                    break
                            
    print(result)
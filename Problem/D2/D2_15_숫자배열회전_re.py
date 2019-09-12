for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(input().split()))

    a = []
    for y in range(N):
        result = ''
        for x in range(N - 1, -1, -1):
            result += board[x][y]
        a.append(result)

    b = []
    for x in range(N - 1, -1, -1):
        result = ''
        for y in range(N - 1, -1, -1):
            result += board[x][y]
        b.append(result)

    c = []
    for y in range(N - 1, -1, -1):
        result = ''
        for x in range(N):
            result += board[x][y]
        c.append(result)

    total = [a, b, c]  # [['741', '852', '963'], ['987', '654', '321'], ['369', '258', '147']]
    for j in range(N):
        for i in range(N):
            print(total[i][j], end=' ')
        print()

for t in range(int(input())):
    N, M, K = map(int, input().split())
    board = []
    for n in range(N):
        data = list(map(int, input().split()))
        board.append(data)

    result = []
    for row in range(N - K + 1):
        for col in range(M - K + 1):
            print(row, col)
            total = 0
            for k in range(K):
                total += board[row][col + k]
                total += board[row + k][K - 1 + col]
                total += board[K - 1 + row][col + k]
                total += board[row + k][col]
            total -= board[row][col]
            total -= board[row][K - 1 + col]
            total -= board[K - 1 + row][col]
            total -= board[K - 1 + row][K - 1 + col]
            result.append(total)
    print('#{} {}'.format(t+1, max(result)))
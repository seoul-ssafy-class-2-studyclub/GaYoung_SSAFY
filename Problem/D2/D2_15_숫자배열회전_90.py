def turn(board):
    ls = []
    for y in range(N):
        result = ''
        for x in range(N - 1, -1, -1):
            result += board[x][y]
        ls.append(result)
    return ls

for t in range(int(input())):
    N = int(input())

    board = []
    for n in range(N):
        board.append(list(input().split()))

    bd_90 = turn(board)  # ['741', '852', '963']
    bd_180 = turn(bd_90)  # ['987', '654', '321']
    bd_270 = turn(bd_180)  # ['369', '258', '147']

    for n in range(N):
        print(bd_90[n], bd_180[n], bd_270[n])

def game(x, y, place):
    global cnt
    if (x, y) == (N - 1, N - 1):
        cnt += 1
        return 0
    else:
        if place == 0:
            if y + 1 < N:
                if board[x][y + 1] == 0:
                    game(x, y + 1, 0)
            if x + 1 < N and y + 1 < N:
                if board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x +1][y + 1] == 0:
                    game(x + 1, y + 1, 2)
        elif place == 1:
            if x + 1 < N:
                if board[x + 1][y] == 0:
                    game(x + 1, y, 1)
            if x + 1 < N and y + 1 < N:
                if board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x +1][y + 1] == 0:
                    game(x + 1, y + 1, 2)
        if place == 2:
            if y + 1 < N:
                if board[x][y + 1] == 0:
                    game(x, y + 1, 0)
            if x + 1 < N:
                if board[x + 1][y] == 0:
                    game(x + 1, y, 1)
            if x + 1 < N and y + 1 < N:
                if board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x +1][y + 1] == 0:
                    game(x + 1, y + 1, 2)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
i = 0
j = 1
game(i, j, 0)
print(cnt)
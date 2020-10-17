def robot():
    for i in range(R):
        if board[i][0] == -1:
            return [i, 0], [i + 1, 0]

def munji():
    check = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] >= 5:
                val = 0
                # 위쪽
                if i - 1 >= 0 and board[i - 1][j] != -1:
                    check[i - 1][j] += board[i][j] // 5
                    val += board[i][j] // 5
                # 오른쪽
                if j + 1 < C and board[i][j + 1] != -1:
                    check[i][j + 1] += board[i][j] // 5
                    val += board[i][j] // 5
                # 아래쪽
                if i + 1 < R and board[i + 1][j] != -1:
                    check[i + 1][j] += board[i][j] // 5
                    val += board[i][j] // 5
                # 왼쪽
                if j - 1 >= 0 and board[i][j - 1] != -1:
                    check[i][j - 1] += board[i][j] // 5
                    val += board[i][j] // 5
                check[i][j] -= val

    for i in range(R):
        for j in range(C):
            board[i][j] += check[i][j]


def clean():
    # up
    state = board[up[0]][C - 1]
    # 오른쪽

    # 위쪽
    # 왼쪽
    # 아래쪽

    # down
    # 오른쪽
    # 아래쪽
    # 왼쪽
    # 위쪽


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

up, down = robot()
for _ in range(T):
    munji()
    # clean()
    print(board)

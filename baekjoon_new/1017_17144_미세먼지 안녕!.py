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
    # 오른쪽 - 위쪽 - 왼쪽 - 아래쪽 반대 순으로 진행!!!!
    # 아래쪽
    for i in range(up[0] - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    # 왼쪽
    for i in range(C - 1):
        board[0][i] = board[0][i + 1]
    # 위
    for i in range(up[0]):
        board[i][C - 1] = board[i + 1][C - 1]
    # 오른쪽
    for i in range(C - 1, 0, -1):
        board[up[0]][i] = board[up[0]][i - 1]
    board[up[0]][1] = 0  # 공기청정기에서 나온바람으로 바로 옆칸은 0이 된다.

    # down
    # 오른쪽 - 아래쪽 - 왼쪽 - 위쪽 반대 순으로 진행!!!!
    # 위쪽
    for i in range(down[0] + 1, R - 1):
        board[i][0] = board[i + 1][0]
    # 왼쪽
    for i in range(C - 1):
        board[R - 1][i] = board[R - 1][i + 1]
    # 아래쪽
    for i in range(R - 1, down[0], -1):
        board[i][C - 1] = board[i - 1][C - 1]
    # 오른쪽
    for i in range(C - 1, 1, -1):
        board[down[0]][i] = board[down[0]][i - 1]
    board[down[0]][1] = 0

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

up, down = robot()
for _ in range(T):
    munji()
    clean()

answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)
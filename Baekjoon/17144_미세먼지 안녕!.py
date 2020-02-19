near = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def spread():
    bd = [row[:] for row in board]

    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                robot.append((i, j))
            if board[i][j] > 0:
                temp = board[i][j] // 5
                for a, b in near:
                    ii, jj = i + a, j + b
                    if 0 <= ii < N and 0 <= jj < M:
                        if board[ii][jj] != -1:
                            bd[ii][jj] += temp
                            bd[i][j] -= temp

    # board를 바뀐 bd와 같게 만들기
    for i in range(N):
        for j in range(M):
            board[i][j] = bd[i][j]

    return bd


def rotate():
    pass







N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

robot = []  # [(2, 0), (3, 0)]
for t in range(T):
    spread()
    # rotate()

print(robot)
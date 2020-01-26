near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def out_air(i, j):
    for a, b in near:
        ii, jj = i + a, j + b
        if 0 <= ii < N and 0 <= jj < M and board[ii][jj] == 0:
            board[ii][jj] = 2
            out_air(ii, jj)


def melt():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                for a, b in near:
                    xi, yi = i + a, j + b
                    if 0 <= xi < N and 0 <= yi < M and board[xi][yi] == 2:
                            board[i][j] = 3

    for i in range(N):
        for j in range(M):
            if board[i][j] == 3:
                board[i][j] = 2

    return 1

def count_cheeze():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cheeze = N * M

board[0][0] = 2
out_air(0, 0)
hour = 0
rs = 0

while cheeze != 0:

    cheeze = count_cheeze()

    if cheeze:
        rs = cheeze
    else:
        break

    hour += melt()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                for a, b in near:
                    ii, jj = i + a, j + b
                    if 0 <= ii < N and 0 <= jj < M and board[ii][jj] == 2:
                        board[i][j] = 2
                        out_air(i, j)
    for b in board:
        print(b)
    print('=====================================')



print(hour)
print(rs)
'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''
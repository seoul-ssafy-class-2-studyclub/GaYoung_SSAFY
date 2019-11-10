from collections import deque

def average():
    sum_num = 0
    cnt = 0
    for n in range(N):
        for m in range(M):
            if board[n][m] != 0:
                sum_num += board[n][m]
                cnt += 1
    mean_num = sum_num / cnt
    print(mean_num)
    for n in range(N):
        for m in range(M):
            if board[n][m] != 0 and board[n][m] > mean_num:
                board[n][m] -= 1
            elif board[n][m] != 0 and board[n][m] < mean_num:
                board[n][m] += 1

    return board

def change():
    global flag
    q = deque()
    for n in range(N):
        for m in range(M):
            if board[n][m] != 0:
                q.append([n, m])
                ls = [[n, m]]
                while q:
                    x, y = q.popleft()
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < N and -1 <= yi < M:
                            if yi == -1:
                                yi = M
                            elif yi == M:
                                yi = -1
                            elif board[xi][yi] == board[x][y] and [xi, yi] not in ls:
                                q.append([xi, yi])
                                ls.append([xi, yi])

                # 인접한 경우가 있다면, flag=1하고 0으로 값 바꾸기
                if len(ls) >= 2:
                    flag = 1
                    for i, j in ls:
                        board[i][j] = 0


N = 4
M = 4
board = [[0, 0, 0, 3], [0, 4, 2, 5], [5, 3, 0, 0], [0, 0, 0, 0]]
near = [(-1, 0), (1, 0), (0, -1), (0, 1)]
average()
change()
for b in board:
    print(b)


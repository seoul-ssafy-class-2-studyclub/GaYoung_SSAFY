from collections import deque

def bfs():
    pass



N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0


total = [0]
total_num = []

while total:
    total = []
    total_num = []
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            q = deque()
            if board[i][j] != 0 and not visit[i][j]:
                ls = [(i, j)]
                ls_total = [board[i][j]]
                q.append((i, j))
                visit[i][j] = True
                while q:
                    x, y = q.popleft()
                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < N and 0 <= yi < N and not visit[xi][yi]:
                            if L <= abs(board[xi][yi] - board[x][y]) <= R:
                                q.append((xi, yi))
                                ls.append((xi, yi))
                                ls_total.append(board[xi][yi])
                                visit[xi][yi] = True

                if len(ls) != 1:
                    total.append(ls)
                    total_num.append(ls_total)

    if len(total_num) == 0:
        break
    else:
        for i in range(len(total_num)):
            mymean = total_num[i] // total[i]
            for y, x in total[i]:
                board[y][x] = mymean

    cnt += 1
print(cnt)

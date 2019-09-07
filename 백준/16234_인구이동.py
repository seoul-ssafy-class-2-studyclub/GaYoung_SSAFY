from sys import stdin
from pprint import pprint

N, l, r = map(int, stdin.readline().split())
board = []
for n in range(N):
    board.append(list(map(int, stdin.readline().split())))

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
            queue = []
            ls = []
            ls_num = []
            if board[i][j] != 0 and not visit[i][j]:
                queue.append((i, j))
                visit[i][j] = True
                ls.append([i, j])
                ls_num.append(board[i][j])
                while queue:
                    x, y = queue.pop(0)
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < N and 0 <= yi < N and not visit[xi][yi]:
                            if l <= abs(board[x][y] - board[xi][yi]) <= r:
                                visit[xi][yi] = True
                                queue.append((xi, yi))
                                ls.append([xi, yi])
                                ls_num.append(board[xi][yi])


                if len(ls) != 1:
                    total.append(ls)
                if len(ls_num) != 1:
                    total_num.append(ls_num)

    if len(total_num) == 0:
        break
    else:
        for t in range(len(total_num)):
            mysum = sum(total_num[t])
            mylen = len(total_num[t])
            mymean = mysum // mylen
            for y, x in total[t]:
                board[y][x] = mymean

    cnt += 1

print(cnt)
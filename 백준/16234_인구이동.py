from sys import stdin
from pprint import pprint

N, l, r = map(int, stdin.readline().split())
board = []
for n in range(N):
    board.append(list(map(int, stdin.readline().split())))

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]



cnt = 0
total = []
total_num = []
while len(total) < 1:
    total = []
    total_num = []
    queue = []
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
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

    for t in total_num:
        mysum = sum(t)
        mylen = len(t)
    mymean = mysum // mylen

    for tot in total:
        for t in tot:
            board[t[0]][t[1]] = mymean
    cnt += 1
pprint(board)
print(cnt)
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(a, b):
    global cnt, res

    while stack:
        x, y, total = stack.pop()
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < N:
                if board[xi][yi] == 1:
                    cnt += 1
                    board[xi][yi] = 0

    return cnt


N = int(input())
board = [list(map(int, input())) for _ in range(N)]


stack = []
cnt_ls = []
res = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            res = 0
            stack.append((i, j, 0))
            cnt = 1
            board[i][j] = 0
            res.append(dfs(i, j))
# print(total)
print(res)
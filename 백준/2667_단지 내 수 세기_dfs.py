# dfs, bfs 모두 가능!
N = int(input())
board = [list(map(int, input())) for _ in range(N)]


near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
stack = []
cnt_ls = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            stack.append((i, j))
            board[i][j] = 0
            cnt = 1
            while stack:
                x, y = stack.pop()
                for a, b in near:
                    xi, yi = (x + a, y + b)
                    if 0 <= xi < N and 0 <= yi < N:
                        if board[xi][yi] == 1:
                            cnt += 1
                            board[xi][yi] = 0
                            stack.append((xi, yi))
            cnt_ls.append(cnt)
cnt_ls.sort()

print(len(cnt_ls))
for n in cnt_ls:
    print(n, end=' ')
print()

from collections import deque

near = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs():
    global cnt
    while q:
        x, y = q.popleft()
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < N:
                if board[xi][yi] == 1:
                    cnt += 1
                    board[xi][yi] = 0
                    q.append((xi, yi))

    return cnt


N = int(input())
board = []
for n in range(N):
    board.append(list(map(int, input())))

cnt_ls = []
res = 0

q = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            q.append((i, j))
            board[i][j] = 0
            cnt = 1
            res += 1
            cnt_ls.append(bfs())

print(res)
cnt_ls.sort()
for c in cnt_ls:
    print(c)
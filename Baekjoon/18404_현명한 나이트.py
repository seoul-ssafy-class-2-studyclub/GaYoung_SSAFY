from collections import deque

N, M = map(int, input().split())

board = [[0] * N for _ in range(N)]
visit = [[False] * N for _ in range(N)]

k1, k2 = map(int, input().split())
board[k1-1][k2-1] = 1

e_cnt = 1
for m in range(M):
    e1, e2 = map(int, input().split())
    e_cnt += 1
    board[e1-1][e2-1] = e_cnt

near = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
cnt_list = ['0'] * M
cnt = 0
q = deque([])
# 1. k가 갈 수 있는 곳 표시!
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            q.append((i, j))
            visit[i][j] = True
            board[i][j] = 0

while q:
    cnt += 1
    for i in range(len(q)):
        x, y = q.popleft()

        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < N and not visit[xi][yi]:
                q.append((xi, yi))
                visit[xi][yi] = True

                if board[xi][yi] != 0:
                    cnt_list[board[xi][yi]-2] = str(cnt)
                    board[xi][yi] = 0

    if '0' in cnt_list:
        continue
    else:
        break

print(' '.join(cnt_list))


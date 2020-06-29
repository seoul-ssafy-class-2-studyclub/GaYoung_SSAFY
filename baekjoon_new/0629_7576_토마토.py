'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
import collections

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]

near = [(0, -1), (0, 1), (1, 0), (-1, 0)]

q = collections.deque()  # 그냥 q로하니까 시간초과 떠서 deque로 수정
for i in range(M):
    for j in range(N):
        if board[i][j] == 1:
            q.append((i, j, 0))
            board[i][j] = 1

while q:
    x, y, cnt = q.popleft()
    for a, b in near:
        xi, yi = x + a, y + b
        if 0 <= xi < M and 0 <= yi < N and board[xi][yi] == 0:
            # cnt += 1 해버리면,, q가 완전히 다 돌때마다 1이 더해져야하는데, q하나 빠질 때마다 다 더해짐,,
            # -> 해결책 : cnt를 들고다녀라.
            board[xi][yi] = 1
            q.append((xi, yi, cnt + 1))

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            cnt = -1
            break

print(cnt)
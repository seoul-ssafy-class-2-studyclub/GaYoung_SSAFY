'''
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
'''
from collections import deque
from pprint import pprint
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = [(0, 0)]
board[0][0] = 1
time = 0
print(q)
while q:
    if time > T:
        break

    time += 1
    for i in range(len(q)):
        x, y = q.pop(0)
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < M:
                if board[xi][yi] == 0:
                    board[xi][yi] = 1
                    q.append((xi, yi))
                elif board[xi][yi] == 2:
                    if time + abs(xi - N + 1) + abs(yi - M + 1) <= T:
                        time = time + abs(xi - N + 1) + abs(yi - M + 1)


print(time)
# 0 0 0 0;0 1 1 0;0 0 1 0;0 0 0 0
put = input()
board = []
for i in put:
    temp = []
    if i == '1' or i == '0':
        temp.append(int(i))
    elif i == ';':
        break
    board.append(temp)
print(board)
bd = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

from collections import deque

queue = deque()
N = len(bd)
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(N):
    for j in range(N):
        if bd[i][j] == 0:
            queue.append((i,j))

while queue:
    x, y = queue.popleft()

    if 1 <= x < N-1 and 1 <= y < N-1:
        if bd[x+1][y] == 1 and bd[x][y+1] == 1 and bd[x-1][y] == 1 and bd[x][y-1] == 1:
            bd[x][y] = 3
            continue

    for a, b in near:
        xi, yi = (x + a, y + b)
        if 0 <= xi < N and 0 <= yi < N and bd[xi][yi] == 1:
            bd[x][y] = 2

cnt = 4
for i in range(N):
    for j in range(N):
        if bd[i][j] == 2:
            cnt += 1

print(cnt)
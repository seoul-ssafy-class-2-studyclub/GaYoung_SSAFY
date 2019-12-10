'''
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
'''

'''
MST 불가! why? 
    최소거리한다고 되는 것이 아님
    . 2 .
    1   4  일때 1 -> 2 -> 4로 되어야하는데
    . 3 .  mst는 1 -> 2 -> 3순으로 간다.
'''
from collections import deque

w, h = map(int, input().split())

board = [list(input()) for _ in range(h)]
dusts = []

for i in range(h):
    for j in range(w):
        if board[i][j] == 'o':
            board[i][j] = 0
            dusts.append((i, j))
        elif board[i][j] == '*':
            dusts.append((i, j))
print(dusts)

for i in range(len(dusts)):
    board[dusts[i][0]][dusts[i][1]] = (i + 1)

for b in board:
    print(b)

adj = [[0] * (len(dusts) + 1) for _ in range(len(dusts) + 1)]
# for a in adj:
#     print(a)

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 1일때 bfs한번 돌고 그에 따른 길이 구해서 인접행렬에 값 적기

for i in range(len(dusts)):
    q = deque(dusts[i])
    # while q:
    #     x, y = q.

print(q)



















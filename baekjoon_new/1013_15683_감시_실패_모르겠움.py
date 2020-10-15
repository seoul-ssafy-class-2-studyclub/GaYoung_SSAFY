camera = {1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
          2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
          3: [[(0, 1), (-1, 0)], [(1, 0), (0, 1)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]],
          4: [[(0, -1), (1, 0), (-1, 0)], [(0, 1), (1, 0), (-1, 0)], [(0, 1), (0, -1), (-1, 0)], [(0, 1), (0, -1), (1, 0)]],
          5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]]}

'''
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
'''
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv = deque([])
cctv_cnt = 0
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv.append([i, j, board[i][j]])
            cctv_cnt += 1

result = 9999999999999999999999999999999999

def check(bd, x, y, go):  # go: 2번camera의 2개방향중 하나 ([(0, 1), (0, -1)])
    for a, b in go:
        xi, yi = x, y
        while True:
            xi += a
            yi += b
            if 0 <= xi < N and 0 <= yi < M:
                if bd[xi][yi] == 0:
                    bd[xi][yi] = '#'
                elif bd[xi][yi] == 6:
                    break
            else:
                break


def bfs():
    bd = deepcopy(board)


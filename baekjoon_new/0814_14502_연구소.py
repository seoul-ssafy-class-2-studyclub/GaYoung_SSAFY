from collections import deque
from itertools import combinations

'''
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
'''


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(board)

can_wall = []
virus = deque([])
cnt = 0  # 빈칸을 모두 cnt에 추가하고, 벽인 경우, 바이러스 지나간 곳에 가면 cnt -= 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            can_wall.append([i, j])
            cnt += 1
        elif board[i][j] == 2:
            virus.append([i, j])

walls = list(combinations(can_wall, 3))  # [([0, 0], [0, 1], [0, 2]), ([0, 0], [0, 1], [0, 3]),,,

for wall in walls:
    
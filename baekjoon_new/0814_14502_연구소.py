from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


can_wall = []
# virus = deque([])
virus = []
cnt = 0  # 빈칸을 모두 cnt에 추가하고, 벽인 경우, 바이러스 지나간 곳에 가면 cnt -= 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            can_wall.append([i, j])
            cnt += 1
        elif board[i][j] == 2:
            virus.append([i, j])

def move(virus):
    answer = 0
    virus = virus[:]  # 함수를 돌릴 때마다 바이러스가 있는거를 써야하니까 새로운 virus가 필요함 -> 복사
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while virus:
        # x, y = virus.popleft()
        x, y = virus.pop(0)

        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < M:
                if bd[xi][yi] == 0:
                    virus.append([xi, yi])
                    answer += 1
                    bd[xi][yi] = 2

    return answer

walls = list(combinations(can_wall, 3))  # [([0, 0], [0, 1], [0, 2]), ([0, 0], [0, 1], [0, 3]),,,


mymax = 0
for i in walls:
    bd = deepcopy(board)
    for j in range(3):
        a = i[j][0]
        b = i[j][1]
        bd[a][b] = 1
    result = cnt - 3 - move(virus)

    if mymax < result:
        mymax = result

print(mymax)
import itertools

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

virus = []
can_wall = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            can_wall.append((i, j))

wall = list(itertools.combinations(can_wall, 3))
for w in wall:
    

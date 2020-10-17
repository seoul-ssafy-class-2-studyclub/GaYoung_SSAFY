from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def eat_fish(shark):
    for i in range(N):
        for j in range(N):
            if 0 < board[i][j] < shark:
                return True

    return False

shark = 2
fish = deque([])
x, y = 0, 0  # shark는 하나니까 x, y를 값으로만 가지고 다닌다.
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            x, y = i, j
        elif 1 <= board[i][j] <= 6:
            fish.append([i, j])


near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while fish:
    visit = [[0] * N for _ in range(N)]
    visit[x][y] = -1



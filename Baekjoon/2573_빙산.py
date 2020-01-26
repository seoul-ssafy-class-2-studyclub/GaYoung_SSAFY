from sys import stdin
from pprint import pprint


# arctic에서 사방면중 0인 갯수 빼고 지나간 곳의 visit을 True로 바꿔준다.
def bfs(x, y):
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    queue = [(x, y)]
    visit[x][y] = True

    while queue:
        x, y = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < M and not visit[xi][yi]:
                if arctic[xi][yi] == 0:
                    arctic[x][y] -= 1
                    if arctic[x][y] < 0:
                        arctic[x][y] = 0
                elif arctic[xi][yi] >= 1:
                    queue.append((xi, yi))
                    visit[xi][yi] = True
    return 1


N, M = map(int, stdin.readline().split())
arctic = []
for n in range(N):
    arctic.append(list(map(int, stdin.readline().split())))


cnt = 0
year = -1
while cnt < 2:
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    finish = False
    for i in range(N):
        for j in range(M):
            if arctic[i][j] > 0 and not visit[i][j]:
                cnt += bfs(i, j)
                finish = True
    year += 1
    if finish == False:
        year = 0
        break

print(year)

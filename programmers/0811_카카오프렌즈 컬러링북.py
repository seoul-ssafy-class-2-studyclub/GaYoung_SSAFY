from collections import deque

def solution(m, n, picture):
    answer = []
    return answer


m, n = 6, 4
picture = [
    [1, 1, 1, 0],
    [1, 2, 2, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 3],
    [0, 0, 0, 3]]

near = [(0, 1),(1, 0),(0, -1),(-1, 0)]
visit = [[0 for _ in range(n)] for _ in range(m)]
print(visit)
total = 0

q = deque()
for i in range(m):
    for j in range(n):
        if picture[i][j] != 0:
            q.append([i, j])

def bfs():
    answer = 0
    while q:
        x, y = q.popleft()
        temp = picture[x][y]

        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < m and 0 <= yi < n and visit[xi][yi] == 0:
                pass




    return answer

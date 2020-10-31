from collections import deque

def solution(v):
    def bfs(q, n, val):
        near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            for a, b in near:
                xi, yi = x + a, y + b
                if 0 <= xi < n and 0 <= yi < n and v[xi][yi] == val and visit[xi][yi] == 0:
                    q.append([xi, yi])
                    visit[xi][yi] = 1

    n = len(v)
    visit = [[0] * n for _ in range(n)]

    cnt_mu = 0
    cnt_goguma = 0
    cnt_gamza = 0

    for i in range(n):
        for j in range(n):
            if v[i][j] == 0 and visit[i][j] == 0:
                val = v[i][j]
                q = deque([[i, j]])
                bfs(q, n, val)
                cnt_mu += 1

            elif v[i][j] == 1 and visit[i][j] == 0:
                val = v[i][j]
                q = deque([[i, j]])
                bfs(q, n, val)
                cnt_goguma += 1

            elif v[i][j] == 2 and visit[i][j] == 0:
                val = v[i][j]
                q = deque([[i, j]])
                bfs(q, n, val)
                cnt_gamza += 1

    answer = [cnt_mu, cnt_goguma, cnt_gamza]
    # print(answer)
    return answer

# v = [[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]
v = [[0,0,1],[2,2,1],[0,0,0]]




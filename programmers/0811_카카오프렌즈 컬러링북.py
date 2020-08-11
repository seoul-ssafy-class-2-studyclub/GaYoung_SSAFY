from collections import deque
from copy import deepcopy

def solution(m, n, picture):
    near = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # visit = [[0 for _ in range(n)] for _ in range(m)]
    pic = deepcopy(picture)
    # print(visit)
    mymax = 0
    q = deque()
    cnt = 0
    result = []
    for i in range(m):
        for j in range(n):
            if picture[i][j] != 0:
                q.append([i, j])
                cnt += 1

                answer = 0
                while q:
                    x, y = q.popleft()
                    temp = pic[x][y]
                    # print(temp)

                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < m and 0 <= yi < n and picture[xi][yi] == temp:
                            picture[xi][yi] = 0
                            q.append([xi, yi])
                            answer += 1
                    # print(q)

                if mymax < answer:
                    mymax = answer

    result.append(cnt)
    result.append(mymax)
    # print(result)

    return result


m, n = 6, 4
picture = [
    [1, 1, 1, 0],
    [1, 2, 2, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 3],
    [0, 0, 0, 3]]


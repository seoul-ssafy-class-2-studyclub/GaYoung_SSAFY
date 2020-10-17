'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
'''

'''
[로직]

'''

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
wall = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j, 0])
        elif board[i][j] == 1:
            wall += 1

len_virus = len(virus)
result = list(combinations(virus, M))
total = len(result)  # 어떤 경우에서도 바이러스 퍼뜨릴 수 없으면 -1
near = [(1, 0), (-1, 0), (0, 1), (0, -1)]
mymin = 999999999999999999999999999999999999999999999
for i in result:
    print(i)
    visit = [[0] * N for _ in range(N)]
    for dx, dy, dcnt in i:
        visit[dx][dy] = '*'

    q = deque(i)

    temp = 0
    while q:
        x, y, cnt = q.popleft()
        temp = cnt

        # "활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다."
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < N:
                if visit[xi][yi] == 0:
                    if board[xi][yi] == 0:
                        visit[xi][yi] = cnt + 1
                        q.append([xi, yi, cnt + 1])
                    if board[xi][yi] == 2:
                        pass
                        

                elif visit[xi][yi] == 1 and board[xi][yi] == 0:
                    if visit[xi][yi] > cnt:
                        visit[xi][yi] = cnt + 1
                        q.append([xi, yi, cnt + 1])
    print(temp)
    print(visit)
    print('----------------')
#     zero = 0
#     for w in range(N):
#         count = visit[w].count(0)
#         zero += count
#
#     if zero == wall + len_virus - M:
#         if mymin > temp:
#             mymin = temp
#
#     else:
#         total -= 1
#
# if total == 0:
#     print(-1)
# else:
#     print(mymin)

'''
11 2
1 1 0 1 1 1 1 1 0 1 1
1 1 2 1 1 1 1 1 2 1 1
0 1 2 1 1 1 0 1 2 1 1
0 1 0 1 1 1 0 1 0 1 1
0 0 2 0 0 1 0 0 2 0 0
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1

4
'''
from collections import deque
from pprint import pprint

near = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def bfs(i, j):
    global a


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

q = deque()
delete = deque()
queue = deque()
aa = 0
year = 0


while aa < 2:
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                q.append((i, j))
                cnt = 0
                while q:
                    x, y = q.popleft()
                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < N and 0 <= yi < M:
                            if board[xi][yi] == 0:
                                cnt += 1
                delete.append((i, j, cnt))


    # 이때 len(delete)를 하면 밑에서 pop을 해도 len(delete)는 이미 값으로 나와있어서 변화가 없음
    # pop하면 len(delete)값은 변화 없고, delete는 하나씩 없어짐
    for d in range(len(delete)):
        x, y, z = delete.popleft()
        board[x][y] -= z
        if board[x][y] <= 0:
            board[x][y] = 0

    # pprint(board)

    aa = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visit[i][j] == False:
                queue.append((i, j))
                aa += 1
                while queue:
                    x, y = queue.popleft()
                    if visit[x][y] == False:
                        visit[x][y] = True
                        for a, b in near:
                            xi, yi = x + a, y + b
                            if 0 <= xi < N and 0 <= yi < M:
                                if board[xi][yi] != 0 and visit[xi][yi] == False:
                                    queue.append((xi, yi))
    year += 1

    if aa == 0:
        year = 0
        break

print(year)

# pprint(board)
# print(a)
# print(year)

# pprint(board)

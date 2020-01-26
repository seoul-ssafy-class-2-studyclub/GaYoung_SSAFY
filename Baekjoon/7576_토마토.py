import collections

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# print(tomato)

queue = collections.deque()
# print(queue)

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            # cnt를 들고 다니면, x, y, cnt를 pop으로 뽑아낼 때 계속 0이기때문에, near한번 돌면 바뀐 xi, yi위치의 cnt는 모두 +1로 값이 동일
            queue.append((i, j, 0))

while queue:
    x, y, cnt = queue.popleft()
    for a, b in near:
        xi, yi = (x + a, y + b)
        if 0 <= xi < N and 0 <= yi < M:
            if tomato[xi][yi] == 0:
                tomato[xi][yi] = 2
                queue.append((xi, yi, cnt + 1))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            cnt = -1
            break
print(cnt)
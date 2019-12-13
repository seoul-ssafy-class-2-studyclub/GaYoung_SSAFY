# 처음에 양분은 모든 칸에 5만큼
# 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
#
# 1. 봄: 자신의 나이만큼 양분을 먹고 나이가 1증가함(1x1크기의 칸에 있는 양분만 먹을 수 있음)
#        하나의 칸에 여러개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
#        땅의 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없다면, 즉시 죽는다
# 2. 여름: 봄에 죽은 나무가 양분으로 변함
#         죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가됨(소수점 버림 -> //)
# 3. 가을: 나무 번식 -> 나무의 나이가 5배수여야하고, 인접한 8개 칸에 나이가 1인 나무가 생김
# 4. 겨울: 양분 추가 -> A[r][c]이며 입력으로 주어짐
# Q. K년이 지난 후 상도의 땅에 살아있는 나무의 개수 구하기

from collections import deque
from heapq import heappush, heappop

def spring():
    global cnt

    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                x = heappop(tree[i][j])
                if x < energy[i][j]:
                    energy[i][j] -= x
                    x += 1
                    heappush(tree[i][j], x)
                elif x > energy[i][j]:
                    cnt -= 1  # 즉시 죽음
                    death.append((i, j, x))

def summer():
    for i in range(len(death)):
        xx, yy, agee = death.popleft()
        energy[xx][yy] += agee // 2


# 3. 가을: 나무 번식 -> 나무의 나이가 5배수여야하고, 인접한 8개 칸에 나이가 1인 나무가 생김
near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def fall():
    global cnt
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < N and 0 <= yi < N:
                            heappush(tree[xi][yi], 1)
                            cnt += 1

def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += insert_energy[i][j]


N, M, K = map(int, input().split())
insert_energy = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
energy = [[5] * N for _ in range(N)]

for m in range(M):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

cnt = M
death = deque()
for k in range(K):
    spring()
    summer()
    fall()
    winter()

print(cnt)
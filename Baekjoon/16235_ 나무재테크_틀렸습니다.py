from collections import deque
from heapq import heappush

'''
1. 봄
   1-1. 봄에는 나무가 자신의 나이만큼 양분을 먹고 나이는 1씩 증가.
   1-2. 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있음
   1-3. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹음-> 번식 후 특히 중요!
   1-4. 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽음
'''


# 나무 나이를 따로 뽑아내서 -> 양분을 먹을 수 있으면 양분 먹고 다시 tree에 넣고
#                       -> 양분을 먹을 수 없어서 죽으면 tree에 넣지 않음
# why? 나무가 죽을 때 pop해버리니까 error가 많이 남. pop하면 len이 계속 달라지기 때문
def spring():
    global cnt
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                z = tree[i][j].popleft()
                if tree[i][j] and energy[i][j] >= z:
                    energy[i][j] -= z
                    tree[i][j][k] += 1
                    tree[i][j].append(z)
                elif tree[i][j] and energy[i][j] < z:
                    cnt -= 1
                    death.append((i, j, k))

'''
2. 여름(죽었을때만)
   2-1. 봄에 죽은 나무가 양분으로 변함
   2-2. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가(소수점 아래는 버림 -> //)
'''
def summer():
    for i in range(len(death)):
        # 죽은 나무의 나이에 대한 정보를 빼왔기 때문에 이 값을 가지고 양분으로 추가하기 때문에
        # 따로 pop을 하지 않아도 되며, for문에서 error를 일으키지 않음
        x, y, z = death.popleft()
        energy[x][y] += z // 2


'''
3. 가을(나무번식)
   3-1. 번식하는 나무는 나이가 5의 배수, 인접한 8개의 칸에 나이가 1인 나무가 생김 -> near8개
'''
near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def fall():
    global cnt
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for a, b in near:
                        xi, yi = (i + a, j + b)
                        if 0 <= xi < N and 0 <= yi < N:
                            heappush(tree[xi][yi], 1)
                            # heappush를 썼다는 것은 heapq를 사용했다는 것!
                            cnt += 1
# heapq: from heapq import heappush, heappop으로 사용하며
#        숫자를 넣을 때, 가지고있는 값보다 작으면 왼쪽으로, 크면 오른쪽으로 넣어주며
#        숫자를 빼낼 때, 작은 값부터 빼낸다.

'''
4. 겨울(양분 추가)
   4-1. 추가되는 양분의 양은 A[r][c] -> 이것이 M개의 줄로 나타남
'''
def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += insert_energy[i][j]

# 디버깅 print
def debug():
    for i in tree:
        print(i)



N, M, K = map(int, input().split())

energy = [[5] * N for _ in range(N)]
insert_energy = [list(map(int, input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

cnt = M
death = deque()


for k in range(K):
    spring()
    # debug()
    summer()
    fall()
    winter()

print(cnt)


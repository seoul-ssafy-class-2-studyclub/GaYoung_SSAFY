'''
5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
'''

from collections import deque

N, M, K = map(int, input().split())
insert_energy = [list(map(int, input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
energy = [[5] * N for _ in range(N)]

for m in range(M):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

dead = deque()  # 여름때 양분으로 바뀌면 새로 죽은 나무 확인해야함
                # -> spring에 넣지 않고 summer에서 빼가면서 진행

# answer = 살아남은 나무의 수 -> spring에서 나무 죽음. summer에서 dead 초기화 fall에서 나무 생성
# cnt를 spring에서 더할게아니라 처음 있던 나무 수를 가지고 4계절 돌면서 + - 하는게 best일듯
cnt = M

'''
봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
'''
def spring():
    global cnt
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):  # 나무 여러개 -> 어린나무부터 먹음
                x = tree[i][j].popleft()  # 어린나무의 나이
                if x <= energy[i][j]:
                    energy[i][j] -= x  # 양분 먹었으면 그만큼 줄어들어야함
                    tree[i][j].append(x+1)
                else:
                    dead.append([i, j, x])  # 즉시 죽음
                    # 여름에서 특정위치에 양분으로 추가되므로 위치+값을 dead에 넣어야함.
                    cnt -= 1


'''
여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
'''
def summer():
    if dead:
        for i in range(len(dead)):
            x, y, t = dead.popleft()
            energy[x][y] += t // 2

'''
가을에는 나무가 번식한다.
번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
'''
near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def fall():
    global cnt
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for a, b in near:
                        xi, yi = i + a, j + b
                        if 0 <= xi < N and 0 <= yi < N:
                            tree[xi][yi].append(1)
                            cnt += 1

'''
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
'''
def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += insert_energy[i][j]

for k in range(K):
    spring()
    summer()
    fall()
    winter()
print(cnt)
# cnt를 계속 들고다녀야지 최종 cnt가 나온다. 아니면 계속 리뉴얼됨. cnt

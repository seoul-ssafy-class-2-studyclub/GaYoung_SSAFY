'''
[풀이방법]
0. 나무는 기본적으로 양분을 모든 칸에 5만큼 가지고있음
1. 봄
   1-1. 봄에는 나무가 자신의 나이만큼 양분을 먹고 나이는 1씩 증가.
   1-2. 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있음
   1-3. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹음-> 번식 후 특히 중요!
   1-4. 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽음
2. 여름(죽었을때만)
   2-1. 봄에 죽은 나무가 양분으로 변함
   2-2. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가(소수점 아래는 버림 -> //)
3. 가을(나무번식)
   3-1. 번식하는 나무는 나이가 5의 배수, 인접한 8개의 칸에 나이가 1인 나무가 생김 -> near8개
4. 겨울(양분 추가)
   4-1. 추가되는 양분의 양은 A[r][c] -> 이것이 M개의 줄로 나타남
'''

# 제발 보통 내용을 지울 때 돌면서 pop하지 말고!! 하나의 리스트에 모아서 나중에 한꺼번에 pop해라!!!

from pprint import pprint
from collections import deque
from heapq import heappush

N, M, K = map(int, input().split())

energy = [[5] * N for _ in range(N)]
insert_energy = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

cnt = M

'''
1. 봄
   1-1. 봄에는 나무가 자신의 나이만큼 양분을 먹고 나이는 1씩 증가.
   1-2. 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있음
   1-3. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹음-> 번식 후 특히 중요! -> ok
   1-4. 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽음
'''

'''
2. 여름(죽었을때만)
   2-1. 봄에 죽은 나무가 양분으로 변함
   2-2. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가(소수점 아래는 버림 -> //)
'''

def spring_summer():
    global cnt
    death =[]  # 제발 보통 내용을 지울 때 돌면서 pop하지 말고!! 하나의 리스트에 모아서 나중에 한꺼번에 pop해라!!!
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j] and energy[i][j] >= tree[i][j][k]:
                    energy[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                elif tree[i][j] and energy[i][j] < tree[i][j][k]:
                    energy[i][j] += tree[i][j][k] // 2
                    cnt -= 1
                    death.append((i, j, k))

    for i in range(len(death)):
        x, y, z = death.pop(0)
        tree[x][y].pop(z)


'''
3. 가을(나무번식)
   3-1. 번식하는 나무는 나이가 5의 배수, 인접한 8개의 칸에 나이가 1인 나무가 생김 -> near8개
'''
near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def fall():
   global cnt
   q = deque()
   for i in range(N):
       for j in range(N):
           for k in range(len(tree[i][j])):
               if tree[i][j][k] % 5 == 0:  # 5배수
                   q.append((i, j))
                   while q:
                       x, y = q.popleft()
                       for a, b in near:
                           xi, yi = (x + a, y + b)
                           if 0 <= xi < N and 0 <= yi < N:
                               heappush(tree[xi][yi],1)
                               cnt += 1

'''
4. 겨울(양분 추가)
   4-1. 추가되는 양분의 양은 A[r][c] -> 이것이 N개의 줄로 나타남
'''
def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += insert_energy[i][j]


for k in range(K):
    print('start')
    pprint(tree)
    pprint(energy)
    print(cnt)
    print('===========================')
    spring_summer()
    print('spring_summer')
    pprint(tree)
    pprint(energy)
    print(cnt)
    print('===========================')
    fall()
    print('fall')
    pprint(tree)
    pprint(energy)
    print(cnt)
    print('===========================')
    winter()
    print('winter')
    pprint(tree)
    pprint(energy)
    print(cnt)
    print('===========================')
print(cnt)
'''
5 2 3
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
13

5 2 4
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
13

5 2 5
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
13

5 2 6
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
85
'''
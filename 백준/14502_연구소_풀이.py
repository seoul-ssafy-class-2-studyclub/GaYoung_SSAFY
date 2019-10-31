'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
9

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
3
'''

'''
[풀이방법]
1. 0은 빈 칸, 1은 벽, 2는 바이러스 // 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
2. 새로 벽을 3개 세운다. -> 조합!! (함수로 직접 만들기!) -> def wall()
   2-1. 벽이 될 수 있는 빈칸을 모아둔 리스트 따로 만들기
3. 가능한 벽 조합일 때, 벽을 세우고 그 후에 바이러스 돌리기 -> def safe()
4. 가능한 안전 영역의 최대 크기를 출력 (mymax로 갱신)
'''

from collections import deque

# 가능한 벽 조합 만들기
result = []
def wall(arr, k):
    if len(arr) == 3:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(can_wall)):
            wall(arr + [can_wall[idx]], idx)
# result = [[[0, 1], [0, 2], [0, 3]], [[0, 1], [0, 2], [0, 6]],,,]


# 벽 3개가 추가된 후, 안전영역 갯수세기
# q를 인자로 가지고와야하는 이유?!
def safe(safe_cnt, q):
    # 한번 돌고나면, q가 빈칸이 되기 때문에, 계속 처음 q를 가지고와서 진행해야함
    queue = [i for i in q]
    while queue:
        x, y = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < M:
                if new_board[xi][yi] == 0:
                    new_board[xi][yi] = 2
                    queue.append((xi, yi))
                    safe_cnt -= 1
    return safe_cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
new_board = [row[:] for row in board]
near = [(-1, 0), (1, 0), (0, 1), (0, -1)]

can_wall = []
q = deque()
safe_cnt = 0

# 일단, 0은 0대로(벽으로 바꿀 수 있는 것 찾기위해), 2는 2대로 모아두기
for i in range(N):
    for j in range(M):
        if new_board[i][j] == 0:
            safe_cnt += 1
            can_wall.append([i, j])
        elif new_board[i][j] == 2:
            q.append((i, j))

# print(q)
# print(safe_cnt)

wall([], -1)  # for result

mymax = 0
# 벽을 세운다음 바이러스 퍼뜨리기
for r in result:
    for s in range(3):
        a = r[s][0]
        b = r[s][1]
        new_board[a][b] = 1
    # safe_cnt에서 벽 3개 추가한 것을 빼줘야한다.
    total = safe(safe_cnt - 3, q)
    # print(total)
    new_board = [row[:] for row in board]
    if mymax < total:
        mymax = total
print(mymax)

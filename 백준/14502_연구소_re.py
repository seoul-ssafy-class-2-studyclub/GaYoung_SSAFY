import copy
from collections import deque

#----------------------------------------------------------------------------------------------------
# 바이러스 퍼지는 함수 -> 그래서 안전한 곳은 몇개?
def safe_place(cnt, queue):

    ######<배운 것>######
    # 만약 safe_cnt를 global로 가지고오면 밑에 for문에서 이 함수가 돌기 때문에
    # safe_cnt가 초기화되지 못한 상태로 계속 값이 줄어든다
    # 그래서 함수의 인자로 받아와야함!!!

    queue = queue[:]
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    virus_cnt = 0

    while queue:
        x, y = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < M:
                if new_board[xi][yi] == 0:
                    queue.append((xi, yi))
                    new_board[xi][yi] = 2
                    virus_cnt += 1
    return cnt - virus_cnt - 3


# 벽을 세우는 함수 -> 가능한 여러 곳 중에서 3곳 선정하기
result = []
def is_wall(arr, k):
    if len(arr) == 3:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(can_wall)):
            is_wall(arr + [can_wall[idx]], idx)

# is_wall([], -1)
# print(result)  # [[[0,1],[0,2],[0,3]][[0,1],[0,2],[0,6]],,]
#----------------------------------------------------------------------------------------------------

N, M = map(int, input().split())
board = []
for n in range(N):
    board.append(list(map(int, input().split())))
new_board = copy.deepcopy(board)

safe_cnt = 0
can_wall = []
queue = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            safe_cnt += 1
            can_wall.append([i, j])
        elif board[i][j] == 2:
            queue.append((i, j))

# 가능한 벽 조합!
is_wall([], -1)

# 벽을 세우고 나서 바이러스 퍼지기!
mymax = 0
for i in result:  # [[0,1],[0,2],[0,3]]
    for j in range(3):
        a = i[j][0]
        b = i[j][1]
        new_board[a][b] = 1
    res = safe_place(safe_cnt, queue)
    if mymax < res:
        mymax = res
    new_board = [row[:] for row in board]  # deepcopy와 동일

    ######<배운 것>######
    # 위에서 new_board = copy.deepcopy(board)를 해주었지만, 그래서 밑에까지 내려오면서 사용 -> 재사용 불가!
    # new_board를 초기화시켜주어야 하기 때문에 새로 board를 deepcopy해준다
    # 만약 new_board = board라고 쓰면 board에 new_board에서 바뀐 값들이 board로 그대로 들어가기 때문에 초기화를 시킬 수 없다!


print(mymax)

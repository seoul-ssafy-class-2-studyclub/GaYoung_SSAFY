import copy

# 벽을 세울 조합 함수
result = []
def is_wall(arr, k):
    if len(arr) == 3:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(can_wall)):
            is_wall(arr + [can_wall[idx]], idx)

# 바이러스 퍼지는 함수
def safe_place(cnt, queue):

    queue = queue[:]
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        x, y = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < M:
                if new_board[xi][yi] == 0:
                    queue.append((xi, yi))
                    new_board[xi][yi] = 2
                    cnt -= 1
    return cnt


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

is_wall([], -1)
# print(result)  # [[[0,1],[0,2],[0,3]][[0,1],[0,2],[0,6]],,]
mymax = 0
for i in result:
    for j in range(3):
        a = i[j][0]
        b = i[j][1]
        new_board[a][b] = 1
    res = safe_place(safe_cnt - 3, queue)
    if res > mymax:
        mymax = res
    new_board = [row[:] for row in board]
print(mymax)

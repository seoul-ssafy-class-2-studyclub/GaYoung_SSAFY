from collections import deque

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
change = {0: 3, 1: 0, 2: 1, 3: 2}
back = {0: 2, 1: 3, 2: 0, 3: 1}

# 벽=1,청소=2,빈칸=0

def bfs(x, y, d):
    q = deque([[x, y, d]])
    cnt = 1
    board[x][y] = 2
    while q:
        row, col, d = q.popleft()

        for i in range(4):
            d = change[d]  # d값을 바꿔야함 -> 변수 다르게하면(direction) d=direction이라고 마지막에 제시해야함
            xi, yi = row + near[d][0], col + near[d][1]  # 여기서 d는 방향바뀌어있는 것

            if 0 <= xi < N and 0 <= yi < M and board[xi][yi] == 0:
                cnt += 1
                board[xi][yi] = 2  # 청소
                q.append([xi, yi, d])
                break

            elif i == 3:  # for문을 돌지 못한경우 -> 갈 곳 없음
                new_xi, new_yi = row + near[back[d]][0], col + near[back[d]][1]
                q.append([new_xi, new_yi, d])

                if board[new_xi][new_yi] == 1:
                    return cnt

print(bfs(x, y, d))

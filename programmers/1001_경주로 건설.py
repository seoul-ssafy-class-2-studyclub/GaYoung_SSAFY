# board = [[0,0,0],[0,0,0],[0,0,0]]  #900
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]  #3800
# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]  #2100
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]  # 3200

from collections import deque

# 도로 가격 정하기
def calculate_cost(now, nextt, cost):
    if (now == 'r' or now == 'l') and (nextt == 'r' or nextt == 'l'):
        return cost + 100

    elif (now == 'd' or now == 'u') and (nextt == 'd' or nextt == 'u'):
        return cost + 100

    elif (now == 'r' or now == 'l') and (nextt == 'd' or nextt == 'u'):
        return cost + 600

    elif (now == 'd' or now == 'u') and (nextt == 'r' or nextt == 'l'):
        return cost + 600


def solution(board):
    answer = []
    N = len(board)

    def bfs(xx, yy, dd, cc):
        near = [(0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'), (-1, 0, 'u')]
        q = deque([[xx, yy, dd, cc]])
        visit = [[0] * N for _ in range(N)]
        visit[0][0] = 1

        while q:
            x, y, direction, costs = q.popleft()

            if x == N - 1 and y == N - 1:
                answer.append(costs)

            for a, b, d in near:
                xi, yi = x + a, y + b
                new_cost = calculate_cost(direction, d, costs)
                if 0 <= xi < N and 0 <= yi < N and board[xi][yi] == 0:
                    if visit[xi][yi] == 0 or visit[xi][yi] > new_cost:  # 작은 값으로 계속 갱신해줘야함
                        visit[xi][yi] = new_cost
                        q.append([xi, yi, d, new_cost])

    bfs(0, 0, 'd', 0)
    bfs(0, 0, 'r', 0)

    return min(answer)


print(solution(board))
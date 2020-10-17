from collections import deque

# bfs로 돌면서 하니까 테케8번 시간초과,, 효율성 시간초과,,
def solution1(m, n, puddles):
    near = [(0, 1), (1, 0)]
    board = [[0] * m for _ in range(n)]
    # print(board)
    cnt = 0
    q = deque([[0, 0, 0]])
    while q:
        x, y, count = q.popleft()
        if x == n - 1 and y == m - 1:
            cnt += 1

        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < n and 0 <= yi < m and board[xi][yi] == 0:
                if [yi, xi] in puddles:
                    continue
                else:
                    q.append([xi, yi, count + 1])
        # print(q)
    return cnt % 1000000007

# m, n = 4, 3
# puddles = [[2, 2]]  # return 4

m=4
n=3
puddles = [[1,3],[3,1]]

def solution(m, n, puddles):
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [j, i] in puddles:
                board[i][j] = 0
            else:
                board[i][j] = board[i][j-1] + board[i-1][j]

    return board[n][m] % 1000000007

print(solution(m, n, puddles))

N, L, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

visit = [[0] * N for _ in range(N)]
near = [(0, 1),(0, -1),(1, 0),(-1, 0)]
# for i in range(N):
#     for j in range(N):
#         if board[i][j]
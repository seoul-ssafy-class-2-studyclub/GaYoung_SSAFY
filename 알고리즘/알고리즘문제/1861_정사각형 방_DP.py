# 모든 방을 돌면서 상하좌우로 향하는데, 현재보다 +1인 곳으로만 이동한다.
# 재귀 함수를 작성해 cnt를 넘겨준다. -> 이때, cnt는 cache의 value값이 된다. // 시작방번호도 항상 들고있는다.


# # 방법1: 전체 cache를 만들어 그 곳에서 value값이 최대이고 key값이 최소인 것을 구한다.
# near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# def dfs(x, y):
#     result = 1  # result가 dfs에 걸리면 +1이 되고, 걸리지않으면(길이없으면) 그대로 1 나옴
#                 # 이때는 cnt가 필요 없음 -> result가 cnt역할을 함
#     for a, b in near:
#         xi = x + a
#         yi = y + b
#         if 0 <= xi < N and 0 <= yi < N:
#             if board[xi][yi] == board[x][y] + 1:
#                 result = 1 + dfs(xi, yi)
#     return result  # 길의 갯수
#
# for t in range(int(input())):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     cache = {}
#     for x in range(N):
#         for y in range(N):
#             if board[x][y]:
#                 cache[board[x][y]] = dfs(x, y)  # cache완성 -> board[x][y]: key, dfs(x, y): value
#
#     minkey = N ** 2 + 1
#     maxvalue = 0
#     for key, value in cache.items():
#         if maxvalue < value:
#             maxvalue = value
#             minkey = key
#         elif maxvalue == value:
#             if minkey > key:
#                 minkey = key
#     print('#{} {} {}'.format(t + 1, minkey, maxvalue))



# 방법2: cache 완성본을 따로 만들지 않고, 방 갯수의 최댓값과 가장 작은 방번호를 계속적으로 갱신한다.
for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    cache = {}
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                cache[board[x][y]] = dfs(x, y)  # cache완성 -> board[x][y]: key, dfs(x, y): value

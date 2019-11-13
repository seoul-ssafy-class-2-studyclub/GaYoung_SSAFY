import itertools
arr = [1, 2, 3, 4, 5]
for k in range(len(arr)+1):
    res = list(itertools.combinations(arr, k))
    print(res)

for r in res:
    print(list(r))

# import collections
# from pprint import pprint
#
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# cnt = 0
# near = [(-1, 0), (0, 1), (0, -1), (1, 0)]
# q = collections.deque()
#
#
# q.append((0, 0))
#
# while q:
#
#     x, y = q.popleft()
#     if board[x][y] == 0:
#         cnt += 1
#         board[x][y] = 2
#         for a, b in near:
#             xi, yi = x + a, y + b
#             if 0 <= xi < N and 0 <= yi < M and board[xi][yi] == 0:
#                 q.append((xi, yi))
#
# print(cnt)
# pprint(board)

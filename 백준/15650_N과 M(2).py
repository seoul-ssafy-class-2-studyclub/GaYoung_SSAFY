N, M = map(int, input().split())

# result = []
# numbers = [i for i in range(1, N + 1)]
# visit = [False] * (len(numbers) + 1)
# def permutation(arr):
#     if len(arr) == N:
#         result.append(arr)
#         return result
#
#     else:
#         for idx in range(len(numbers)):
#             if visit[idx]:
#                 continue
#             elif visit[idx] == False:
#                 visit[idx] = True
#                 permutation(arr + [numbers[idx]])
#                 visit[idx] = False
#
# ans = permutation([])
# print(ans)

from itertools import combinations

n, m = map(int, input().split())
for k in combinations([i for i in range(1, n+1)], m):
    print(" ".join(map(str, k)))

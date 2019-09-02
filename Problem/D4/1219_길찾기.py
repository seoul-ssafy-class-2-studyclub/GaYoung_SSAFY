# 길이 있으면 1
# 길이 없으면 0
# def dfs(adj):
#     visit = [False] * 100
#     stack = []
#     stack.append(0)
#     while stack:
#         n = stack.pop()
#         if not visit[n]:
#             visit[n] = True
#             for i in adj:
#                 if adj[i][99] == 1:
#                     return 1
#         stack.append(adj[n])
#     return 0

for t in range(1):
    case, N = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[0] * 100 for i in range(100)]

    for d in range(0, N * 2, 2):
        adj[data[d]][data[d+1]] += 1

    print('#{} {}'.format(case, dfs(adj)))

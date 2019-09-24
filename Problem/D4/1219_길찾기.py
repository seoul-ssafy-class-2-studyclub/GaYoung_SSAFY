def dfs(adj):
    visit = [False] * 100
    stack = []
    stack.append(0)

    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node] = True
        for i in adj:
            if i[99] == 1:
                return 1
        stack.append(adj[node])
    return 0

for t in range(1):
    case, N = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[0] * 100 for i in range(100)]

    for d in range(0, N * 2, 2):
        adj[data[d]][data[d+1]] += 1
    
    # print(adj)

    print('#{} {}'.format(case, dfs(adj)))





# def dfs(adj):
#     visit = [False] * 100
#     stack = []
#     stack.append(0)
#     while stack:
#         node = stack.pop()
#         if not visit[node]:
#             visit[node] = True
#             if visit[99] == 1:
#                 return 1
#         stack.extend(adj[node])
#     return 0

# for t in range(1):
#     case, N = map(int, input().split())
#     data = list(map(int, input().split()))
#     adj = [[] for i in range(100)]
#     for i in range(0, N * 2, 2):
#         adj[data[i]].append(data[i + 1])

#     print('#{} {}'.format(case, dfs(adj)))
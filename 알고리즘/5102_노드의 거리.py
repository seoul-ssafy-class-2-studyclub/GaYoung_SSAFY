for t in range(int(input())):
    V, E = map(int, input().split())
    data = []
    for e in range(E):
        data.append(list(map(int, input().split())))
    start, end = map(int, input().split())

    visit = [False] * (V + 1)
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        adj[data[i][0]].append(data[i][1])
        adj[data[i][1]].append(data[i][0])

    queue = [start]
    flag = 0
    while queue:
        node = queue.pop(0)
        if node == end:
            break
        if visit[node] == False:
            visit[node] = True
            queue.extend(adj[node])

    print('#{} {}'.format(t+1, visit.count(True)))
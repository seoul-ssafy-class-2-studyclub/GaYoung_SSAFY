for t in range(int(input())):
    V, E = map(int, input().split())
    data = []
    for e in range(E):
        data.append(list(map(int, input().split())))
    start, end = map(int, input().split())

    visit = []
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        adj[data[i][0]].append(data[i][1])
        adj[data[i][1]].append(data[i][0])

    cnt = 0
    queue = [start, -1]
    while queue:
        node = queue.pop(0)
        if node == end:
            break
        if node not in visit and node != -1:
            visit.append(node)
            queue.extend(adj[node])
        elif node == -1:
            queue.append(node)
            cnt += 1
            if queue[0] == -1:
                cnt = 0
                break

    print('#{} {}'.format(t + 1, cnt))

def dfs(adj):
    visit = [False] * (v + 1)  #  index가 0~6까지 있어야 visit[start], visit[end] 작성 가능!
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node] = True
            if visit[start] and visit[end]:
                return 1
            stack.extend(adj[node])
    return 0


for t in range(int(input())):
    v, e = map(int, input().split())
    board = []
    for i in range(e):
        data = list(map(int, input().split()))  # 1->4, 1->3으로 간다는 의미 -> adj다시 만들어야함!
        board.append(data)
    start, end = map(int, input().split())
    adj = [[] for i in range(v + 1)]
    for a in board:
        adj[a[0]].append(a[1])
    # print(adj)  #[[], [4, 3], [3, 5], [], [6], [], []]

    print('#{} {}'.format(t+1, dfs(adj)))
    
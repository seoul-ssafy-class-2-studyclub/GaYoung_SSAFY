def relation(n):
    global visit

    visit[n] = True

    for a in adj[n]:
        if visit[a] == False:
            relation(a)
    return


for t in range(int(input())):
    N, M = map(int, input().split())

    data = []
    for m in range(M):
        word = list(map(int, input().split()))
        data.append(word)

    visit = [False] * (N + 1)
    adj = [[] for _ in range(N + 1)]
    for i in data:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])  # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

    cnt = 0
    for n in range(1, N + 1):
        if visit[n] == False:
            relation(n)
            cnt += 1

    print('#{} {}'.format(t+1, cnt))
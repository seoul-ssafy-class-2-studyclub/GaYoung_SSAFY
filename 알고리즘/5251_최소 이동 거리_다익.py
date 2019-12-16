# 다익스트라 알고리즘 적용 문제
for t in range(int(input())):
    N, E = map(int, input().split())

    w_list = [0] * (N + 1)
    adj = [{} for i in range(N+1)]

    for e in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w

    visit = [False for i in range(N+1)]
    distance = [1e9 for i in range(N+1)]
    distance[0] = 0

    while True:
        min_dist = 1e9
        curent_idx = -1

        if visit[N] == True:
            break

        for i in range(N+1):
            if visit[i] == False and min_dist > distance[i]:
                curent_idx = i
                min_dist = distance[i]
        visit[curent_idx] = True

        for key, val in adj[curent_idx].items():
            if visit[key] == False and distance[key] > min_dist + val:
                distance[key] = min_dist + val

    print('#{} {}'.format(t+1, distance[N]))
for t in range(int(input())):
    N = int(input())
    visit = [0] * (N + 1)
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort()

    for n in range(1, N+1):
        if visit[n] != 0:
            continue

        for m in range(n+1, N+1):

            if score[n-1][1] < score[m-1][1]:
                visit[m] += 1
                # vis[m] = True

    cnt = -1
    for v in visit:
        if v == 0:
            cnt += 1
    print(visit)
    print(cnt)
    print('-----------------------------------------')
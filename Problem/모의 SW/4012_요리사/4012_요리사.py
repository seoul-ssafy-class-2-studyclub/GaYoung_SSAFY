import itertools

for t in range(int(input())):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]

    cnt = N // 2
    menu = set(n for n in range(N))

    choose = list(itertools.combinations(menu, cnt))

    mymin = float("inf")
    for cc in range(len(choose)//2):

        first = list(choose[cc])
        second = list(menu - set(choose[cc]))

        for f in range(len(first) // 2):
            m_sum = 0

            fir = list(itertools.combinations(first, 2))
            for a, b in fir:
                m_sum += adj[a][b]
                m_sum += adj[b][a]

            sec = list(itertools.combinations(second, 2))
            for c, d in sec:
                m_sum -= (adj[c][d] + adj[d][c])

            m_sum = abs(m_sum)
            if mymin > m_sum:
                mymin = m_sum

    print('#{} {}'.format(t+1, mymin))

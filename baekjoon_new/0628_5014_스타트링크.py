F, S, G, U, D = map(int, input().split())
visit = [False for _ in range(F+1)]
q = [S]
visit[S] = 1
cnt = 0

while q:
    x = q.pop(0)
    if x == G:
        print(cnt)

    if x + U < F:
        pass

    if x - D >= 0:

import collections

F, S, G, U, D = map(int, input().split())

def bfs():
    if S > G and D == 0:
        return "use the stairs"

    elif S < G and U == 0:
        return "use the stairs"

    q = collections.deque([(S, 0)])
    visit = [0 for _ in range(F + 1)]
    visit[S] = 1

    while q:
        x, cnt = q.popleft()
        if x == G:
            return cnt

        if x + U <= F and not visit[x + U]:
            q.append((x + U, cnt + 1))
            visit[x + U] = 1

        if x - D >= 1 and not visit[x - D]:
            q.append((x - D, cnt + 1))
            visit[x - D] = 1

    return "use the stairs"

print(bfs())
from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

visit = [0] * 100001
cnt = 0
flag = False

while q:

    cnt += 1

    for i in range(len(q)):
        n = q.popleft()

        if n == K:
            flag = True
            break

        next = [n - 1, n + 1, 2 * n]
        for nxt in next:
            if 0 <= nxt <= 100000:
                if visit[nxt] == 0:
                    visit[nxt] = 1
                    q.append(nxt)

    if flag:
        break

print(cnt - 1)

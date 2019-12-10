from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)
k_cnt = 0
cnt = 0
flag = False
while q:
    if 0 <= N <= 500001 and 0 <= K <= 50001:
        visit = [0] * 500001
        for i in range(len(q)):
            n = q.popleft()

            if visit[n + 1] == 0:
                q.append(n + 1)
            elif visit[n - 1] == 0:
                q.append(n - 1)
            elif visit[2 * n] == 0:
                q.append(2 * n)
            if K == n:
                flag = True
                break

        k_cnt += 1
        K += k_cnt
        cnt += 1

        if flag:
            break

    if flag:
        break


if flag:
    print(cnt)
else:
    print(-1)
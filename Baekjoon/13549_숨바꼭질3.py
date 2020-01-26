from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

visit = [0] * 100001
cnt = 0
flag = False
visit[N] = 1

while q:
    # 2*X 위치로 이동
    # ex) 5 19이면 답은 2가 아닌 1!!!!!! -> 10 20 40 80은 다 0초!! -> 20-1=19이므로 답은 1
    # len(q)이므로 10도 넣어주어야하고, 20도 넣어줘야한다.
    # 만약 10을 넣어주지 않으면, len(q)=1에서 그냥 바로 q가 끝나기 때문에, 10도 넣고, 20도 넣으면서 나아가야함.
    for i in range(len(q)):

        n = q.popleft()
        q.append(n)

        nxt = n * 2

        if n == K:
            flag = True
            break

        # while nxt <= 100000:하면 시간초과
        # -> why? 만약 처음에 N이 0으로 주어지면 0 * 2^n해도 계속 0이므로 더 나아갈 수 없음
        while 0 < nxt <= 100000:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
            nxt *= 2

    # X-1, X+1로 이동
    cnt += 1
    for i in range(len(q)):
        n = q.popleft()

        if n == K:
            flag = True
            break

        next = [n - 1, n + 1]
        for nxt in next:
            if 0 <= nxt <= 100000:
                if visit[nxt] == 0:
                    visit[nxt] = 1
                    q.append(nxt)

    if flag:
        break

print(cnt - 1)
from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

visit = [0] * 100001
result, time = 0, 0
flag = False

while q:
    time += 1
    check = []
    for i in range(len(q)):
        n = q.popleft()

        if n == K:
            flag = True
            result += 1

        next = [n - 1, n + 1, 2 * n]
        for nxt in next:
            if 0 <= nxt <= 100000:
                if visit[nxt] == 0:
                    check.append(nxt)
                    q.append(nxt)

    # check라는 리스트에 한번에 넣은다음에 q한번 돌때마다 마지막에 visit을 바꿔야한다.
    # death와 동일!

    # q들어오는법
    # 5 -> 4 6 10 -> 3 5* 8 5* 7 12 9 11 20 -> 2 4* 6* 7* 9* 16 6* 8* 14 11* 13 24 8* 10* 18 10* 12* 22 19 21 40
    # -> 1 3* 4* 15 17 32 13* 15 28 12* 14* 26 23 25 48 17 19* 36 21* 23 44 18* 20* 38 20* 22* 42 39 41 80
    # => 1 15 17 32 15 28 26 23 25 48 17 36 23 44 38 42 39 41 80 (남아있는 q)

    # q를 append시켰으니까 한번에 visit시켜주고 (line 26 + line 40)
    # q에서 빼내면서 K와 같으면 result += 1
    for i in check:
        visit[i] = 1

    if flag:
        break

print(time - 1)
print(result)
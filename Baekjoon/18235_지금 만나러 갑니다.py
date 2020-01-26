from collections import deque

N, A, B = map(int, input().split())
q_A = deque([A])
q_B = deque([B])
y = 0
stop = False

while True:
    visit = [False] * (N+1)
    # 영원히 만나지 못함 -> print(-1)
    if len(q_A) == 0 or len(q_B) == 0:
        break

    move = 2 ** y
    for a in range(len(q_A)):
        x_a = q_A.popleft()
        if 0 < x_a + move <= N:
            q_A.append(x_a + move)
            visit[x_a + move] = True
        if 0 < x_a - move <= N:
            q_A.append(x_a - move)
            visit[x_a - move] = True
    # print('q_A')
    # print(q_A)
    # print(visit)

    for b in range(len(q_B)):
        x_b = q_B.popleft()
        if 0 < x_b + move <= N:
            if not visit[x_b + move]:
                q_B.append(x_b + move)
            else:
                stop = True
                break
        if 0 < x_b - move <= N:
            if not visit[x_b - move]:
                q_B.append(x_b - move)
            else:
                stop = True
                break
    # print('q_B')
    # print(q_B)
    # print(visit)
    # print('=====================================')
    if stop:
        break
    else:
        y += 1

    # if stop:
    #     break

if stop:
    print(y + 1)
else:
    print('-1')
    # print('===========================================')

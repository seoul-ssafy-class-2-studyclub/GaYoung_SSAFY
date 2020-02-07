N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

circle = min(N, M) // 2
for r in range(R):
    # 한번 회전하겠다.
    bd = [row[:] for row in board]
    dx, dy = 1, 0

    for n in range(circle):
        while n == N-1:
            pass




for bb in bd:
    print(' '.join(map(str, bb)))

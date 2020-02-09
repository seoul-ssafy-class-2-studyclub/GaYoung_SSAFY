N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
mymin = min(N, M) // 2
for r in range(R):
    # 한번 회전하겠다.

    bd = [row[:] for row in board]
    for n in range(mymin):
        dx, dy = 1, 0
        temp = bd[n][n]

        while





for bb in bd:
    print(' '.join(map(str, bb)))

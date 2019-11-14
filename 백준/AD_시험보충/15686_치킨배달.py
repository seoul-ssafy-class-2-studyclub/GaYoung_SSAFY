import itertools



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])


result = list(itertools.combinations(chicken, M))
# [([0, 1], [3, 0]), ([0, 1], [4, 0]), ([0, 1], [4, 1]), ([3, 0], [4, 0]), ([3, 0], [4, 1]), ([4, 0], [4, 1])]

answer = 999999999999
for r in result:
    res = 0
    for h in house:
        mymin = 9999999999
        for c in r:
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])

            if mymin > dis:
                mymin = dis
        res += mymin
    if answer > res:
        answer = res
print(answer)
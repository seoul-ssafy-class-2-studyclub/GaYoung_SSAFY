import itertools

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


enermy = []
for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            enermy.append((n, m))

shooter = [(N, k) for k in range(M)]
# print(shooter)  # [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)]

shooter_choose = list(itertools.combinations(shooter, 3))
# print(shooter_choose)

for s in shooter_choose:
    cnt = 0

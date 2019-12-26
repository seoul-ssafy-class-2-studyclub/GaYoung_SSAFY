select_shooter = []
def combination(arr, k):
    if len(arr) == 3:
        select_shooter.append(arr)
        return select_shooter
    else:
        for idx in range(k + 1, len(shooter)):  # 순서 없음 -> 전 값보다 큰 것만 나와야함
            combination(arr + [shooter[idx]], idx)


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
shooter = [(N, k) for k in range(M)]

combination([], -1)

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for select in select_shooter:


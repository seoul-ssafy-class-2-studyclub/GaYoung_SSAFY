select_shooter = []
def combination(arr, k):
    if len(arr) == 3:
        select_shooter.append(arr)
        return select_shooter
    else:
        for idx in range(k + 1, len(shooter)):  # 순서 없음 -> 전 값보다 큰 것만 나와야함
            combination(arr + [shooter[idx]], idx)

def dis(a, b, c, d):
    return abs(a - c) + abs(b - d)

def removeenemy():
    pass


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
shooter = [(N, k) for k in range(M)]


combination([], -1)
print(select_shooter)  # [[(5, 0), (5, 1), (5, 2)], [(5, 0), (5, 1), (5, 3)], [(5, 0), (5, 1), (5, 4)], [(5, 0), (5, 2), (5, 3)], [(5, 0), (5, 2), (5, 4)], [(5, 0), (5, 3), (5, 4)], [(5, 1), (5, 2), (5, 3)], [(5, 1), (5, 2), (5, 4)], [(5, 1), (5, 3), (5, 4)], [(5, 2), (5, 3), (5, 4)]]
enemy = []
for i in range(N-1, -1, -1):
    for j in range(M):
        if board[i][j] == 1:
            enemy.append([i, j])

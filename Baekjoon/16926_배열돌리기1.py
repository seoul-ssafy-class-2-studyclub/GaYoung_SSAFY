
def rotate(r, c):
    # 오른쪽
    for k in range()

    # 아래

    # 왼쪽

    # 위

    return board


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for r in range(R):
    for i in range(N):
        for j in range(M):
            rotate(i, j)

for b in board:
    print(b)

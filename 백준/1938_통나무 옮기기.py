N = int(input())
board = [list(input()) for _ in range(N)]

bbb = []
eee = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            bbb.append((i, j))
        elif board[i][j] == 'E':
            eee.append((i, j))
print(bbb)
visit = [[0] * N for _ in range(N)]

# 통나무 가로=5, 통나무 세로=6
# visited할때 가운데만 표시하기! -> 통나무가 가로로 되어있는지, 세로로 되어있는지

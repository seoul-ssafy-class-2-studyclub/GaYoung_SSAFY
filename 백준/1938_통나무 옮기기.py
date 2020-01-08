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
# print(bbb)  # [(0, 0), (1, 0), (2, 0)]
visit = [[0] * N for _ in range(N)]

# 통나무 가로=5, 통나무 세로=6
# visited할때 가운데만 표시하기! -> 통나무가 가로로 되어있는지, 세로로 되어있는지

if bbb[0][0] == bbb[1][0]:  # 가로 # x값이 같다면 이것은 가로
    visit[bbb[1][0]][bbb[1][1]] = 5
elif bbb[0][1] == bbb[1][1]:  # 세로 # y값이 같다면 이것은 세로
    visit[bbb[1][0]][bbb[1][1]] = 6

print('board')
print(board)
print('visit')
print(visit)
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
row = [(0, -1), (0, 1)]
col = [(-1, 0), (1, 0)]
all = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
# 세로방향: 사방으로 이동할때는 간 곳에서 위아래 확인
# 가로방향: 사방으로 이동할 때 간 곳에서 양옆 확인
# 회전: 이동한 방향에서 8방향 확인

for i in range(N):
    for j in range(N):
        pass







'''
5
B0011
B0000
B0000
11000
EEE00
'''
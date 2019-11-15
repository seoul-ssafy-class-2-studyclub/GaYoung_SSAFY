import collections
from pprint import pprint

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def out_air(x, y):
    for a, b in near:
        if 0 <= x + a < N and 0 <= y + b < M and board[x + a][y + b] == 0:
            board[x + a][y + b] = 2
            out_air(x + a, y + b)


def melt():
    for i in range(N):
        for j in range(M):
            for a, b in near:
                if 0 <= i + a < N and 0 <= j + b < M and board[i][j] == 1:
                    if board[i + a][j + b] == 2:
                        ls.append((i + a, j + b))

    for l in range(len(ls)):
        x, y = ls.pop(0)
        board[x][y] = 2
    return 1


def count_c():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = collections.deque()

board[0][0] = 2
out_air(0, 0)

# pprint(board)
'''
[[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2],
 [2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2],
 [2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
 [2, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2],
 [2, 1, 1, 1, 1, 0, 0, 1, 1, 2, 2, 2],
 [2, 2, 1, 1, 0, 0, 0, 1, 1, 2, 2, 2],
 [2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
 [2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
 [2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
 [2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
'''

cheeze = 1  # 치즈 갯수
queue = collections.deque()
ls = []
hour = 0
last = 0
# while cheeze != 0:
cheeze = count_c()

# if cheeze != 0:
#     last = cheeze
# else:
#     break
#

hour += melt()

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            for a, b in near:
                ii, jj = i + a, j + b
                if 0 <= ii < N and 0 <= jj < M and board[ii][jj] == 2:
                    # 외부공기 시작 칸을 2로 바꾸고 시작
                    board[ii][jj] = 2
                    out_air(ii, jj)


print(ls)
pprint(board)
print(hour)
print(last)


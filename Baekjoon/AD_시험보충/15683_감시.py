from pprint import pprint
from itertools import product

# 함수 안에 있는 board면 전역에서 찾을 수 없음 ->  인자로 넣는다
def right(x, y):
    global temp
    if (y + 1) < M and board[x][y + 1] != 6:
        if board[x][y + 1] == 0:
            board[x][y + 1] = '#'
            temp -= 1
        right(x, y + 1)


def left(x, y):
    global temp
    if 0 <= (y - 1) and board[x][y-1] != 6:
        if board[x][y - 1] == 0:
            board[x][y - 1] = '#'
            temp -= 1
        left(x, y - 1)

def up(x, y):
    global temp
    if 0 <= (x - 1) and board[x - 1][y] != 6:
        if board[x - 1][y] == 0:
            board[x - 1][y] = '#'
            temp -= 1
        up(x - 1, y)


def down(x, y):
    global temp
    if (x + 1) < N and board[x + 1][y] != 6:
        if board[x + 1][y] == 0:
            board[x + 1][y] = '#'
            temp -= 1
        down(x + 1, y)


def cctv():
    if ccttvv == 1:
        if dir == 0:
            right(x, y)
        elif dir == 1:
            left(x, y)
        elif dir == 2:
            up(x, y)
        elif dir == 3:
            down(x, y)

    elif ccttvv == 2:
        if dir == 0:
            right(x, y)
            left(x, y)
        elif dir == 1:
            up(x, y)
            down(x, y)
        elif dir == 2:
            right(x, y)
            left(x, y)
        elif dir == 3:
            up(x, y)
            down(x, y)

    elif ccttvv == 3:
        if dir == 0:
            right(x, y)
            down(x, y)
        elif dir == 1:
            down(x, y)
            left(x, y)
        elif dir == 2:
            left(x, y)
            up(x, y)
        elif dir == 3:
            up(x, y)
            right(x, y)

    elif ccttvv == 4:
        if dir == 0:
            right(x, y)
            down(x, y)
            left(x, y)
        elif dir == 1:
            down(x, y)
            left(x, y)
            up(x, y)
        elif dir == 2:
            left(x, y)
            up(x, y)
            right(x, y)
        elif dir == 3:
            up(x, y)
            right(x, y)
            down(x, y)

    elif ccttvv == 5:
        right(x, y)
        down(x, y)
        left(x, y)
        up(x, y)


N, M = map(int, input().split())
board_ = [list(map(int, input().split())) for _ in range(N)]

ls = []
cnt = N * M
for i in range(N):
    for j in range(M):
        rs = 0
        if board_[i][j] == 6:
            cnt -= 1

        elif 1 <= board_[i][j] <= 5:
            ls.append((i, j, board_[i][j]))
            cnt -= 1

mymin = 99999999999999999999
direction = list(product([0, 1, 2, 3], repeat=len(ls)))
for d in direction:
    board = [row[:] for row in board_]
    temp = cnt
    for i in range(len(ls)):
        x, y, ccttvv = ls[i]
        dir = d[i]  # dir은 0~3까지 가능!
        cctv()


    if mymin > temp:
        mymin = temp
print(mymin)


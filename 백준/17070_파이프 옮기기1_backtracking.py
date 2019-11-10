'''
[풀이방법]
1. right: 1, down: 2, side: 3
   1-1. 1 -> 1, 3 / 2 -> 2, 3 / 3 -> 1, 2, 3
   1-2. 지나가는 칸이 다 빈칸이여야함.
2. 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로
'''

def pipe(i, j, direction):
    global cnt
    # 탈출조건
    if (i, j) == (N - 1, N - 1):
        cnt += 1
        return 1
    else:
        if direction == 1:
            if j + 1 < N:
                if board[i][j + 1] == 0:
                    pipe(i, j + 1, 1)
            if i + 1 < N and j + 1 < N:
                if board[i][j + 1] == 0 and board[i + 1][j] == 0 and board[i + 1][j + 1] == 0:
                    pipe(i + 1, j + 1, 3)
        elif direction == 2:
            if i + 1 < N:
                if board[i + 1][j] == 0:
                    pipe(i + 1, j, 2)
            if i + 1 < N and j + 1 < N:
                if board[i][j + 1] == 0 and board[i + 1][j] == 0 and board[i + 1][j + 1] == 0:
                    pipe(i + 1, j + 1, 3)
        elif direction == 3:
            if j + 1 < N:
                if board[i][j + 1] == 0:
                    pipe(i, j + 1, 1)
            if i + 1 < N:
                if board[i + 1][j] == 0:
                    pipe(i + 1, j, 2)
            if i + 1 < N and j + 1 < N:
                if board[i][j + 1] == 0 and board[i + 1][j] == 0 and board[i + 1][j + 1] == 0:
                    pipe(i + 1, j + 1, 3)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
x = 0
y = 1

pipe(x, y, 1)
print(cnt)

'''
3
0 0 0
0 0 0
0 0 0
1
6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
13
'''
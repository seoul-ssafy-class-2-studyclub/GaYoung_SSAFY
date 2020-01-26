board = [[0 for i in range(10)] for i in range(10)]

def is_color(r1, c1, r2, c2, color):
    if color == 1:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += 1
    if color == 2:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += 2
    return board

for t in range(int(input())):
    board = [[0 for i in range(10)] for i in range(10)]  # 보드 초기화!!!
    N = int(input())
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())  # int, 2 2 4 4 1
        data = is_color(r1, c1, r2, c2, color)
    for r in range(10):
        for c in range(10):
            if data[r][c] >= 3:
                count += 1
    print('#{0} {1}'.format(t+1, count))

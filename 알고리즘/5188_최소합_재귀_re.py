near = [(1, 0), (0, 1)]
def dfs(x, y, result):
    global mymin
    if x == N - 1 and y == N - 1:
        if mymin > result:
            mymin = result
        return mymin

    else:
        for a, b in near:
            xi = x + a
            yi = y + b
            if 0 <= xi < N and 0 <= yi < N:
                dfs(xi, yi, result + board[xi][yi])

for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))
    mymin = 99999
    start = board[0][0]
    dfs(0, 0, start)
    print(mymin)
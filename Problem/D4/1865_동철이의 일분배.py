def dfs(x, success):
    global mymax
    if x == N:
        if mymax < success:
            mymax = success
        return mymax

    if mymax > success:
        return

    for n in range(N):
        if board[x][n] == 0:
            continue
        elif board[x][n] != 0 and visit[n] == False:
            visit[n] = True
            dfs(x + 1, success * board[x][n] / 100)
            visit[n] = False


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    mymax = 0
    success = 1

    dfs(0, 1)

    print('#{} {:.6f}'.format(t+1, mymax*100))
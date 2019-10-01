def func(x, sum=0):
    global mymin

    if x == 6:
        if mymin > sum:
            mymin = sum
            return

    if mymin < sum:
        return

    for i in range(6):
        if not visit[i]:
            visit[i] = True
            func(x + 1, sum + ls_t[x][i])
            visit[i] = False


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(10)]

    robot = []
    snack = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == 9:
                robot.append((i, j))
            elif board[i][j] != 0:
                snack.append((i, j))


    ls_t = []
    for r in robot:
        ls = []
        for s in snack:
            a = abs(r[0] - s[0]) + abs(r[1] - s[1])
            ls.append(a)
        ls_t.append(ls)
    # for i in ls_t:
    #     print(i)

    visit = [False] * 6
    mymin = 99999999999
    func(0)
    print(mymin)
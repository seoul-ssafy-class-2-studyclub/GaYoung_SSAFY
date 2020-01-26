def dfs(x, sum):
    global mymin

    if x == N:  # N=3인 경우, x는 0, 1, 2 -> 이때, 재귀를 쓰므로 2에서 3으로갈 때, 이 if문에 걸림
        if mymin > sum:
            mymin = sum
            return

    if mymin < sum:
        return

    for i in range(N):  # i=0,1,2
        if not visit[i]:
            visit[i] = True
            # print(visit)
            dfs(x + 1, sum + board[x][i])  # x를 하나씩 키워야 x==N에 도달 가능!
            visit[i] = False
            # print(visit)


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    mymin = 999999999999999

    dfs(0, 0)
    print('#{} {}'.format(t + 1, mymin))

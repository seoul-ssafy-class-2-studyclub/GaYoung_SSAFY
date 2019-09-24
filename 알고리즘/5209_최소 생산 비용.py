'''
1. A1-B2-C3을 첫번째 경우의 수로 둔다. (73+59+83)
2. visit = [False] * 3 -> A1 -> visit[0] = True
3. 일단 가능한 경우의 수   mymax = 99999999999와 비교
        1) A1-B2-C3 (73_59_83) -> mymax = 1)
        2) A1-B3-C2 (73+40+31) -> mymax = 2)
        3) B1-A2-C3 (21+11+83) -> mymax = 3)
        4) B1-A3-C1 (21+40+24) -> mymax = 4)
        5) C1-A2-B3 (21+11+31) -> mymax = 5)
        6) C1-A3-B3 (21+59+24) -> A3을 더하면 mymax를 넘음 -> 더 많았다면 backtracking
4. dfs하면서 backtracking
5. 73 21 21  x=0일때, 73을 택하면 visit[0]=True(73, 11, 24)
   11 59 40  dfs를 x=1에서 돌리면 visit[1]=True가 되며,
   24 31 83  그 전인 visit[0]을 다시 False로 두어 돌아올 수 있게 함.
      그럼 어떻게 1에서 0으로 돌아가지 않게할까? for i in range(N)을하며,
      visit[i]를 앞으로만 가게한다.
'''


def dfs(x, sum):
    global mymin

    if x == N:  # x가 점점커져서 마지막줄까지 가서 합을 비교
        if mymin > sum:
            mymin = sum
        return

    if mymin < sum:  # 중간에 5) 6)번 처럼 sum을 더하고있는데, mymin보다 크면 stop?
        return

    for n in range(N):
        if not visit[n]:
            visit[n] = True
            # print(visit)
            dfs(x + 1, sum + board[x][n])
            visit[n] = False
            # print(visit)

for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    mymin = 999999999999

    dfs(0, 0)
    print('#{} {}'.format(t + 1, mymin))
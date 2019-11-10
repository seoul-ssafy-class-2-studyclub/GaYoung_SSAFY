'''
3
1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 9 0 1 0 0 0 0
0 0 0 9 0 2 0 0 0 0
0 0 0 9 0 3 0 0 0 0
0 0 0 9 0 4 0 0 0 0
0 0 0 9 0 5 0 0 0 0
0 0 0 9 0 6 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 6 9 1 0 0 0 0 0
0 0 0 9 2 0 0 0 0 0
0 0 0 9 3 0 0 0 0 0
0 0 0 9 4 0 0 0 0 0
0 0 0 9 5 0 0 0 0 0
0 0 0 9 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
3
0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 9 0 5 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 9 0 2 0 0 0
0 9 0 0 0 0 0 9 0 0
0 0 0 0 0 0 9 0 0 0
0 0 0 3 0 0 0 0 4 0
0 0 0 0 0 6 0 0 0 0
0 0 0 9 0 0 0 0 0 0
'''

'''
[정답]
#1 12
#2 11
#3 16
'''

'''
[풀이방법]
1. 로봇은 로봇대로 모아두고, 과자는 과자대로 모아둔다.
2. 로봇은 상하좌우로 이동하며, 이동이 끝나면 남은 로봇 중 하나가 남은 과자 중 한곳으로 이동
   2-1. 로봇이 이동하는 경로에 다른 로봇이나 목표 과자 이외의 과자가 있는 경우 무시하고 이동
3. 로봇 이동 거리의 합 중 최소값 -> 최소합
'''

# 최소합 구하는 함수
def minimum(x, sum=0):
    global mymin

    if x == 6:
        if mymin > sum:
            mymin = sum
            return

    if mymin < sum:
        return

    for i in range(6):
        if visit[i] == False:
            visit[i] = True
            minimum(x+1, sum+ls_t[x][i])
            visit[i] = False


for t in range(int(input())):
    N = int(input())
    board = []
    for i in range(10):
        board.append(list(map(int, input().split())))

    visit = [False] * 6
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 로봇은 로봇대로, 과자는 과자대로 모아
    robot = []
    snack = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == 9:
                robot.append([i, j])
            elif board[i][j] != 0:
                snack.append([i, j])


    '''
    최소값 찾는 방법
    [1, 1, 2, 3]
    [2, 3, 1, 1]
    [4, 4, 5, 2]
    [2, 3, 1, 5]
    1. 일단 이런 형태로 만든다
    2. visit를 T로 체크해가면서 다시 할때는 visit를 F로 바꿨다가 다시가기
    '''

    # 로봇을 기준으로 과자를 먹으러간다.
    # 로봇 기준으로 과자의 거리 다 구해놓기!
    ls_t = []
    for r in robot:
        ls = []
        for s in snack:
            dis = abs(r[0] - s[0]) + abs(r[1] - s[1])
            ls.append(dis)
        ls_t.append(ls)

    # for l in ls_t:
    #     print(l)
    '''
    [2, 3, 4, 5, 6, 7]
    [3, 2, 3, 4, 5, 6]
    [4, 3, 2, 3, 4, 5]
    [5, 4, 3, 2, 3, 4]
    [6, 5, 4, 3, 2, 3]
    [7, 6, 5, 4, 3, 2]
    '''

    mymin = 9999999999999
    minimum(0)
    print(mymin)
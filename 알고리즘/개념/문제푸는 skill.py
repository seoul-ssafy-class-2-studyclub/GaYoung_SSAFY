'''
[ 1. board에서 가로줄 세로줄을 하나의 리스트에 넣기 ]
[ 하나의 중심점에서 가로세로 값을 리스트에 넣고, 그 리스트들을 하나의 리스트에 넣기 ]

1-1. ls리스트에 중심점 마다의 필요한 값들 넣기 (가로+세로-중심점 / 가로(-중심)+세로(-중심)+중심)
1-2. 중심점 찾기 -> for x in , for y in ran
1-3. 중심점 찾았을 때, for i in ra를 돌리면서 i != y일때 빼고 다 ls에 넣기
1-4. 중심점 찾았을 때, for j in ra를 돌리면서 j != x일때 빼고 다 ls에 넣기
1-5. 중심점마다 ls에 넣고, 초기화시키면서 ls_t에 넣기
'''

for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    ls_t = []
    for x in range(N):
        for y in range(N):
            ls = []
            ls.append(board[x][y])
            for i in range(N):
                if i != y:  # 가로
                    ls.append(board[x][i])
            for j in range(N):
                if j != x:  # 세로
                    ls.append(board[j][y])
            ls_t.append(ls)

'''
[ 문제 분석 시 ]
0. 명세서 제대로 읽기
1. 무조건 상하좌우로 이동한다고 near 사용 X -> 상하좌우로 이동한다는 것은 대각선으로 갈 수 없다는 것!!
2. 반복해서 로봇을 이동시킨다 -> 반복하면 for, while문 사용!
3. 이동거리의 합 중 최솟값 -> 최소합(백트래킹)
'''

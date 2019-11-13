'''
[문제]
0. 배양 용기의 크기는 무한
1. 초기: 비활성 상태, 생명력 수치=X -> X시간 동안 비활성 상태, X시간이 지나는 순간 활성 상태
2. 활성 상태: X시간 동안 살아있을 수 있으며 X시간이 지나면 세포는 죽음(죽은 상태로 해당 그리드 셀을 차지)
    2-1. 활성화된 줄기 세포는 첫 1시간 동안 상, 하, 좌, 우 네 방향으로 동시에 번식
    2-2. 번식된 줄기 세포는 비활성 상태이다.
    2-3. 번식하는 방향에 이미 줄기 세포가 존재하는 경우 해당 방향으로 추가적으로 번식하지 않음
3. 두 개 이상의 줄기 세포가 하나의 그리드 셀에 동시 번식하려고 하는 경우 생명력 수치가 높은 줄기 세포가 해당 그리드 셀을 혼자서 차지하게 된다.
    3-1. list사용할 필요없음

Q. K시간 후 살아있는 줄기 세포(비활성 상태 + 활성 상태)의 총 개수는?
'''

'''
[풀이 방법]
1. 초기: 비활성 상태 -> X시간이 지나면 활성상태가 됨
2. 죽은상태 == 0, 살아있는 줄기세포(비활성+활성) > 0
3. board를 만들고(최대용기크기), start(input값), cell(번식 시 생명력 수치가 높은 줄기 세포 찾기위해)
4. 
'''

'''
2 2 10
1 1
0 2
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
'''

from collections import deque
'''
[번식하기]
1. 
2. 시간이 지나야 번식 가능 ????????????????
3. 죽은상태 = 0, 살아있음 > 0
'''
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def spread():
    for qq in range(len(q)):
        x, y, z = q.popleft()
        # q에는 지금 죽지않은 애들이 들어있음
        if board[x][y] > 0: # 활성상태가 안된애들
            board[x][y] -= 1
            if board[x][y] == 0:
                board[x][y] = -1
            q.append((x, y, z))
        # board[x][y] -= 1
        # if board[x][y] == 0:
        #     board[x][y] = -1
        elif z > 0:  # 딱 활성상태가 된 애들
            # z가 0이 된 순간 빠져야함으로, z > 1

            for a, b in near:
                xi, yi = x + a, y + b
                if board[xi][yi] == 0:  # board[xi][yi]==0인 부분에만 넣을거야
                    if visit[xi][yi] == 0:
                        new.append((xi, yi))
                        visit[xi][yi] = z
                    else:
                        if visit[xi][yi] < z:
                            visit[xi][yi] = z
            if z != 1:
                q.append((x, y, z - 1))  # 여기서 z-1로해가지고 z>1로 해야함
    # deque([(4, 5, 1), (6, 5, 1), (5, 4, 1), (4, 6, 1), (5, 7, 1)])

    for n in range(len(new)):
        x, y = new.popleft()
        board[x][y] = visit[x][y]
        q.append((x, y, board[x][y]))


def debug():
    for i in board:
        print(i)
    print(q)


for t in range(int(input())):
    N, M, K = map(int, input().split())
    start = [list(map(int, input().split())) for _ in range(N)]
    board = [[0 for _ in range(M + K + 100)] for _ in range(N + K + 100)]
    visit = [[0] * (M + K + 100) for _ in range(N + K + 100)]
    q = deque()


    # 가능한 보드판에 초기상태를 넣어주기
    for n in range(N):
        for m in range(M):
            if start[n][m] > 0:  # 초기상태 값들
                temp = start[n][m]
                board[n + K // 2][m + K // 2] = temp
                q.append((n + K // 2, m + K // 2, temp))
                visit[n + K // 2][m + K // 2] = True
    # print(q)  # deque([(5, 5, 1), (5, 6, 1), (6, 6, 2)])



    # 퍼지면서 한 칸에 동시에 번식하면
    for k in range(K):
        new = deque()
        spread()
        # debug()
    print('#{} {}'.format(t+1, len(q)))
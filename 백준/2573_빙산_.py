def bfs(i, j):
    queue.append((i, j))
    visit[i][j] = True
    while queue:
        x, y = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < M and not visit[xi][yi]:
                if board[xi][yi] == 0:
                    board[x][y] -= 1
                    if board[x][y] < 0:
                        board[x][y] = 0
                elif board[xi][yi] >= 1:
                    visit[xi][yi] = True
                    queue.append((xi, yi))
    return 1


N, M = map(int, input().split())  # 5(세로) 7(가로)
board = [list(map(int, input().split())) for _ in range(N)]

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = []
# board를 돌면서 0이 아닌 곳에서 주변이 0인 경우 직접 수를 빼줌.

# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

# 예시에서 2(1,1)가 0이 되고, 4는 3이되어야하는데, 2가 0이 되어서 지금 논리에 따르면 2가 된다.
# 이를 방지하기 위해 visit을 사용해 0이 아닌 곳에 닿았다면, visit을 True로 바꾸고,
# 주변이 0인 곳은 visit을 하면 안됨. why? 다른 곳에서도 사용해야하는 경우 있기 때문!


# 빙산이 두 덩어리 이상으로 분리되는 해를 구하기! -> cnt, year필요!
# for i, for j 한바퀴 돌았을 때, year += 1, cnt += 1
# 이때, visit도 for i, for j 한바퀴 돌았을 때, 초기화해야함

cnt = 0  # 빙산 갯수
         # 이 자리에 cnt = 0이 있어야, while cnt < 2 사용 가능!
         # cnt = 0인데, stack 돌때마다 cnt 갯수 확인해야하므로
         # while cnt<2안에 또 cnt = 0작성
year = -1  # 빙산이 분리되는 시간
           # why? year = -1? -> year = -1이여야 for i, for j가 돌았을 때, year +=1을 하는 것인데
           # cnt = 2가되는 순간에 year+1이 되므로 year = -1로 설정
           # 최종 결과값에서 year-=1을 하게되면, flag=0(덩어리분리되지 않음)일 때, year=1로 둬야함

while cnt < 2:
    visit = [[False] * M for _ in range(N)]
    flag = 0  # 빙산이 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 flag = 1
              # flag = 1이면 0을 print함
    cnt = 0  # 빙산 덩어리 수
             # 매번 초기화되어야함.
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visit[i][j] == False:
                cnt += bfs(i, j)  # stack이 끝나면 cnt += 1인 것이므로,
                                  # 이는 빙산의 갯수를 의미
                flag = 1  # 덩어리가 분리됨을 의미

    year += 1

    if flag == 0:  # 덩어리가 분리되지 않았을 때
        year = 0
        break

print(year)


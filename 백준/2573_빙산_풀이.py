'''
[input]
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''

'''
[풀이방법]
1. board를 돌면서 0이 아닌 곳에서 near을 돌면서 사방이 0일때마다 board[i][j] -= 1
2. visit을 설정해 지나갔던 곳은 가지 않는걸로 <- 근데 칸을 이동할때마다 visit새로해야함(True, False)
3. cnt += 1 -> 실패: 처음에 0아닌수일때 cnt=1이고 한바퀴 다 돌고 새로시작하면 +1
            -> 성공: cnt=0에서 board[i][j]!=0것이 시작하면 cnt += 1 
            -> cnt >= 2 이상이면 stop
4. board를 한바퀴 다 돌면 year+=1
'''

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
near = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs():
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


cnt = 0
year = -1
# year은 board한번 돌고나면 year+=1인 것이므로
# 처음 board돌고나서는 year=0이여야 하므로 year=-1로 두고 설정

# 만약 year=0으로 설정하였다면, 결과에서 -1해주고
# flag == 0일때, year = 1로 설정!(거의 끼워맞추기느낌..ㅎ)

queue = []
while cnt < 2:
    flag = 0
    visit = [[False] * M for _ in range(N)]
    cnt = 0  # cnt는 한바퀴 돌때마다 초기화 되어야함
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visit[i][j]:
                cnt += bfs()
                flag = 1

    year += 1
    if flag == 0:
        year = 0
        break

print(year)
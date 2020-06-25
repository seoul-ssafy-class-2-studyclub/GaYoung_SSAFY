'''
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
'''
N, M, k = map(int, input().split())

shark = [[] for _ in range(M)]
board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            shark[board[i][j] - 1].extend([i, j])
            board[i][j] = [board[i][j], k]

shark_dir = list(map(int, input().split()))
for i in range(M):
    shark[i].append(shark_dir[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

priority = [[] for _ in range(M)]
idx = -1
for i in range(M * 4):  # 시간 많이 소요.. 4개씩 한 묶음이라 생각해서 0 1 2 3이 첫번째 상어로 감
                        # append하고 4로 나뉘어떨어질 때 idx += 1시키기 (이때 0%4=0)
    if i % 4 == 0:
        idx += 1
    priority[idx].append(list(map(int, input().split())))

ans = 0
while True:
    if ans > 1000:
        print(-1)
        break

    '''
    [로직]
    1. 우선순위에 따라 1,2,3,4 상어 이동
    2. 혹시 같은 줄에 상어가 있으면 숫자 큰 상어없어지고, 상어 냄새는 남는다
    3. 다 한바퀴 돌리면 냄새-1 시키기
    '''
    for i in range(M):
        x, y, d = shark[i][0], shark[i][1], shark[i][2]
        for j in range(4):
            direction = priority[i][d-1][j]
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = [i, k]

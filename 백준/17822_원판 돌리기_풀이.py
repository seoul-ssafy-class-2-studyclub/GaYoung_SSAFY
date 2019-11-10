'''
[풀이방법]
1. x 배수, d방향, k칸 : def move
   1-1. 배수 for m in range(M) 돌면서 m %x == 0인 것들 도는데,
   1-2. 방향 0:시계방향, 1:반시계방향
   1-3. k칸 이동
2. 인접하면서 수가 같은 것을 모두 지우기 -> 수가 같으면 0으로 두기 : def change
   2-1. 세로로 같은 것은 board 세로로 보기
      2-1-1. board판을 넘어가면 안됨.
   2-2. 원둘레로 같은 것은 board 가로로 보기
      2-2-1. 왼쪽 오른쪽 모두 check
3. def change에서 인접하면서 수가 같은 것이 없다면, : def average()
    3-1. 평균 22/6 보다 작은 수는 +1, 큰 수는 -1
      
4. 큰 틀
    4-1. board있으면 for t in range(T):
                        move
                        same함수
'''
from collections import deque

def move(x, d, k):
    for n in range(1, N+1):  # 회전할 것이다.(x의 배수인 것에서)
        if n % x == 0:
            if d == 0:  # 시계방향
                left = board[n-1][M-k:]
                right = board[n-1][:M-k]
            else:
                left = board[n-1][k:]
                right = board[n-1][:k]
            board[n-1] = left + right

    return board


def average():
    sum_num = 0
    cnt = 0
    for n in range(N):
        for m in range(M):
            if board[n][m] != 0:
                sum_num += board[n][m]
                cnt += 1
    mean_num = sum_num / cnt

    for n in range(N):
        for m in range(M):
            if board[n][m] != 0 and board[n][m] > mean_num:
                board[n][m] -= 1
            elif board[n][m] != 0 and board[n][m] < mean_num:
                board[n][m] += 1

    return board


def change():
    global flag
    q = deque()
    for n in range(N):
        for m in range(M):
            if board[n][m] != 0:
                q.append([n, m])
                ls = [[n, m]]
                while q:
                    x, y = q.popleft()
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < N and -1 <= yi < M:
                            if yi == -1:
                                yi = M
                            elif yi == M:
                                yi = -1
                            elif board[xi][yi] == board[x][y] and [xi, yi] not in ls:
                                q.append([xi, yi])
                                ls.append([xi, yi])

                # 인접한 경우가 있다면, flag=1하고 0으로 값 바꾸기
                if len(ls) >= 2:
                    flag = 1
                    for i, j in ls:
                        board[i][j] = 0


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
near = [(-1, 0), (1, 0), (0, -1), (0, 1)]


for t in range(T):
    x, d, k = map(int, input().split())
    move(x, d, k)
    for b in board:
        print(b)
    print('======================')
    flag = 0
    change()
    for b in board:
        print(b)
    print('======================')
    if flag != 1:
        average()
    for b in board:
        print(b)
    print('======================')
    print('----------------------------')



result = 0
for n in range(N):
    for m in range(M):
        result += board[n][m]

print(result)

'''
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
30

4 4 2
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
22

4 4 3
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
2 0 2
22

4 4 4
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
2 0 2
3 1 1
0

4 6 3
1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
2 1 4
3 0 1
2 1 2
26
'''
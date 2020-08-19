'''
3 5 10
10 15 20
20 30 25
40 22 10

2 20 50
50 30
20 40
'''

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(0, 1), (0, -1), (1, 0), (-1, 0)]



time = 0

while True:
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and visit[i][j] == 0:
                move = [[i, j]]
                cal = [board[i][j]]  # 나라별 인구 수 넣기
                visit[i][j] = 1
                xy = [[i, j]]  # 좌표 넣기 -> 평균낸 값 바꿔주기 위해

                # 인구이동
                while move:
                    x, y = move.pop(0)
                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < N and 0 <= yi < N and visit[xi][yi] == 0:
                            if L <= abs(board[x][y] - board[xi][yi]) <= R:
                                move.append([xi, yi])
                                cal.append(board[xi][yi])
                                visit[xi][yi] = 1
                                xy.append([xi, yi])
                print('xy')
                print(xy)
                print('cal')
                print(cal)
                print('--------------------------------')

                if len(cal) > 1:
                    myval = sum(cal) // len(cal)
                    for a, b in xy:
                        board[a][b] = myval

                else:
                    break

    time += 1
print(time)
        # print('board')
        # print(board)
        # print(time)
        # print('--------------------------------')

# print(visit)
# print(cal)
# print(board)
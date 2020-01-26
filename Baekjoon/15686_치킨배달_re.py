from sys import stdin
from itertools import combinations as cb

N, M = map(int, input().split())
board = []
for n in range(N):
    board.append(list(map(int, stdin.readline().split())))

# 치킨집, 일반 집 구하기
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i, j])
        elif board[i][j] == 1:
            house.append([i, j])

# 치킨집을 M개 조합으로 구한다면, 치킨집의 조합이 설정되어 있을 때,
# 각자 집에서부터 치킨집까지 가장 가까운 거리를 구하고 모두 합치기(=t)
# t값을 구했으면 치킨집의 조합마다 t값을 구할 수 있다.
# 그 중 min 값을 구하면 됨

rs_d = []
for i in cb(chicken, M):
    rs = 0
    for k in house:
        mymin = 10000
        for j in i:
            res = abs(k[0] - j[0]) + abs(k[1] - j[1])
            if mymin > res:
                mymin = res
        rs += mymin
    rs_d += [rs]
print(min(rs_d))

'''
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
'''

from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 0은 빈 칸, 1은 집, 2는 치킨집
chicken = []
homes = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i, j])
        elif board[i][j] == 1:
            homes.append([i, j])


can_chicken = list(combinations(chicken, M))
mymin = 9999999999999999999999999999999999999

for can in can_chicken:
    distance = 0
    for home in homes:
        myminmin = 9999999999
        for c in can:
            temp = abs(home[0] - c[0]) + abs(home[1] - c[1])
            if myminmin > temp:
                myminmin = temp
                # print(myminmin)

        distance += myminmin

    if mymin > distance:
        mymin = distance

print(mymin)

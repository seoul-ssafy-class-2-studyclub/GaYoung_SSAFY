'''
4 4
.LX.
.X..
....
.L..
'''

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

seats = []
people = []

for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            people.append((i, j))
        elif board[i][j] == 'L':
            seats.append((i, j))

q = [{} for _ in range(R ** 2 + C ** 2)]
# 이때 q에 들어가는 값은 dis기준!

for s1, s2 in seats:
    for p1, p2 in people:
        dis = (s1 - p1) ** 2 + (s2 - p2) ** 2
        # key: seats, value: people -> 하나의 의자에 몇명이 앉을수있도록.
        # 두명 이상이면 cnt += 1(충돌)
        # people, seats 사용되면 visit 표시

        # 의자를 기준으로 사람을 추가할 것이다! -> q[dis].get((s1, s2))
        if q[dis].get((s1, s2)) == None:
            q[dis][(s1, s2)] = [(p1, p2)]
        else:
            q[dis][(s1, s2)].append((p1, p2))
# [{}, {(0, 1): [(0, 2), (1, 1)]}, {}, {}, {(3, 1): [(1, 1)]}, {}, {}, {}, {}, {}, {(3, 1): [(0, 2)]}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

# seats를 for문 돌리면서 people visit 체크하기!
visited = [[False] * C for _ in range(R)]


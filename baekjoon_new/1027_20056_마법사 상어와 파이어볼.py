'''
4 2 1
1 1 5 2 2
1 4 7 1 6
# 8
4 2 2
1 1 5 2 2
1 4 7 1 6
# 8
4 2 2
1 1 5 2 2
1 4 7 1 6
# 0
7 5 3
1 3 5 2 4
2 3 5 2 6
5 2 9 1 7
6 2 1 3 5
4 4 2 4 2
# 9
'''

N, M, K = map(int, input().split())

before_move = {}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    before_move[(r-1, c-1)] = [(m, s, d)]


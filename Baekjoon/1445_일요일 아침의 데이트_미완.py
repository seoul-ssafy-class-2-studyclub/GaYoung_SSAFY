'''
6 6
...g..
g.gFg.
g.....
gg.ggg
......
...S.g
답 : 0 3

10 8
...g.g.g
..Fggggg
.....g..
g.g.g.g.
.g.g.g.g
...g.g.g
g.g.gggg
........
g...g.S.
........
답 : 1 5

7 5
..Fg.
g.g..
..ggg
.g.g.
..S.g
답 : 0 4
'''

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[1e9, 1e9] * M for _ in range(N)]
print(visit)
'''
YYYYY
SYSYS
YYYYY
YSYYS
YYYYY
'''

from itertools import combinations

board = [list(input()) for _ in range(5)]

ls = []
for i in range(5):
    for j in range(5):
        if board[i][j] == 'Y':
            ls.append(1)
        else:  # 이다솜
            ls.append(0)


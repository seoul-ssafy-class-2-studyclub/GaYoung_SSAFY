# x = -4
# y = 13
# a = y % (-x)
# print(a)
# b = y % abs(-x)
# print(b)

'''
NUM -4
DIV
END
2
13
-13

NUM 4
DIV
END
2
13
-13

NUM -4
MOD
END
2
13
-13

NUM 4
MOD
END
2
13
-13

QUIT
'''

# from heapq import heappush, heappop
#
# board = [[[], [2, 2]],[[1, 3], []]]
# for i in range(2):
#     for j in range(2):
#         for k in range(len(board[i][j])):
#             a = heappop(board[i][j])
#             print(a)
#             print('=================')
#             heappush(board[i][j], 4)
#             print(board)
#             print('-------------------')


a = 2 % 6
print(a)
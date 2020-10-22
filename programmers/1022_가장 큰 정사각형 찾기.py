# board = [[0,1,1,1],
#          [1,1,1,1],
#          [1,1,1,1],
#          [0,0,1,0]]

# board = [[0,0,1,1],[1,1,1,1]]
board = [[1,0],[0,0]]

def solution(board):

    row = len(board)
    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] >= 1:
                val = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
                board[i][j] = val

    answer = 0
    for i in range(row):
        for j in range(col):
            if answer < board[i][j]:
                answer = board[i][j]

    # print(answer)
    return answer ** 2

print(solution(board))

# def solution1(board):
#
#     row = len(board)
#     col = len(board[0])
#     mymax = 0
#     for i in range(1, row):
#         for j in range(1, col):
#             # 이런경우는 [[1,0],[0,0]]이면 더이상 진행이 불가함
#             # -> 진행 다 하면 [[1,0],[0,0]]이므로 최대값을 구해야함
#             if board[i][j] >= 1:
#                 val = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
#                 board[i][j] = val
#
#                 if mymax < val:
#                     mymax = val
#
#     return mymax ** 2

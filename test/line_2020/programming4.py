from collections import deque

def solution(maze):
    answer = 0
    return answer

# maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
# maze = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]
# maze = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]


len_maze = len(maze)
board = [[1]*(len_maze+2) for _ in range(len_maze+2)]
for i in range(len_maze):
    for j in range(len_maze):
        board[i+1][j+1] = maze[i][j]
# print(board)
# [[1, 1, 1, 1, 1, 1],
#  [1, 0, 1, 0, 1, 1],
#  [1, 0, 1, 0, 0, 1],
#  [1, 0, 0, 0, 0, 1],
#  [1, 1, 0, 1, 0, 1],
#  [1, 1, 1, 1, 1, 1]]

q = deque([[1, 1, 0]])

while True:

    x, y, cnt = q.popleft()
    if x == len_maze and y == len_maze:
        print(cnt)
        break

    if 0<= x-1 < len_maze+2 and 0<= y-1 < len_maze+2 and 0<= x+1 < len_maze+2 and 0<= y+1 < len_maze+2:
        # 아래로
        if board[x + 1][y] == 0 and board[x][y+1] == 1 and board[x+1][y+1] == 1:
            q.append([x + 1, y, cnt + 1])
            print('down')
        # 아래한칸+오른쪽한칸
        if board[x + 1][y] == 0 and board[x][y+1] == 1 and board[x+1][y+1] == 0:
            q.append([x+1, y+1, cnt + 2])
            print('down+right')

        # 아래한칸+왼쪽한칸
        if board[x][y-1] == 1 and board[x+1][y-1] == 0 and board[x + 1][y] == 0:
            q.append([x + 1, y + 1, cnt + 2])
            print('down+left')

        # 오른쪽한칸 + 위로한칸
        if board[x][y+1] == 0 and board[x-1][y] == 1 and board[x-1][y + 1] == 0:
            q.append([x-1, y + 1, cnt + 2])
            print('right+up')

        # 위로
        if board[x-1][y] == 0 and board[x][y-1] == 1 and board[x - 1][y -1] == 1:
            q.append([x-1, y, cnt + 1])
            print('up')

        # 위로 + 왼쪽
        if board[x-1][y] == 0 and board[x][y-1] == 1 and board[x - 1][y -1] == 0:
            q.append([x - 1, y - 1, cnt + 2])
            print('up+left')

        # 위로 + 오른쪽
        if board[x][y+1] == 1 and board[x-1][y] == 1 and board[x - 1][y + 1] == 0:
            q.append([x - 1, y - 1, cnt + 2])
            print('up+right')

        # 왼쪽 + 아래로
        if board[x][y-1] == 0 and board[x+1][y-1] == 0 and board[x+1][y] == 1:
            q.append([x + 1, y - 1, cnt + 2])
            print('up+left')

        # 오른쪽
        if board[x][y+1] == 0 and board[x+1][y] == 1 and board[x+1][y+1] == 1:
            q.append([x, y+1, cnt + 1])
            print('right')

        # 오른쪽+아래
        if board[x][y + 1] == 0 and board[x + 1][y] == 1 and board[x + 1][y + 1] == 0:
            q.append([x+1, y + 1, cnt + 2])
            print('right+down')

        # 왼쪽
        if board[x][y-1] == 0 and board[x+1][y] == 1 and board[x-1][y] == 1:
            q.append([x, y - 1, cnt + 1])
            print('left')

        # 오른쪽+아래
        if board[x][y + 1] == 0 and board[x + 1][y] == 1 and board[x + 1][y + 1] == 0:
            q.append([x + 1, y + 1, cnt + 2])
            print('left+down')
    #
    # print(q)
    # print('------------------------------')






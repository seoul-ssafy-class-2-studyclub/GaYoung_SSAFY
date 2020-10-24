from collections import deque


def move(first, second, board):
    N = len(board)
    result = []
    # move
    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for a, b in near:
        next1 = (first[0] + a, first[1] + b)
        next2 = (second[0] + a, second[1] + b)

        if 0 <= next1[0] < N and 0 <= next1[1] < N and 0 <= next2[0] < N and 0 <= next2[1] < N:
            if board[next1[0]][next1[1]] == 0 and board[next2[0]][next2[1]] == 0:
                result.append((next1, next2))

    # 가로 turn
    if first[0] == second[0]:
        for d in [1, -1]:
            if 0 <= first[1] < N and 0 <= second[1] < N and 0 <= first[0] + d < N and 0 <= second[0] + d < N:
                if board[first[0] + d][first[1]] == 0 and board[second[0] + d][second[1]] == 0:
                    result.append([first, (first[0] + d, first[1])])
                    result.append([second, (second[0] + d, second[1])])

    else:  # 세로 turn
        for d in [1, -1]:
            if 0 <= first[0] < N and 0 <= second[0] < N and 0 <= first[1] + d < N and 0 <= second[1] + d < N:
                if board[first[0]][first[1] + d] == 0 and board[second[0][second[1] + d]] == 0:
                    result.append([(first[0], first[1] + d), first])
                    result.append([(second[0], second[1] + d), second])

    return result


def solution(board):
    N = len(board)
    q = deque([[(0,0),(0,1),0]])
    print(q)
    check = [[(0, 0), (0, 1)]]

    while q:
        front, end, time = q.popleft()
         # = xy
        print(front, end, time)

        if front == [N-1, N-1] or end == [N-1, N-1]:
            print('final')
            print(front, end, time)
            print(time)
            return time

        for i in move(front, end, board):
            if i not in check:
                print(i)
                q.append([i[0], i[1], time + 1])
                check.append(i)

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
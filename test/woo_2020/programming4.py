from collections import deque


def solution(n, board):
    answer = 0
    total = n ** 2
    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    nums = [i for i in range(1, total+1)]
    q = deque([[0, 0, 0]])

    for i in nums:
        while True:
            x, y, cnt = q.popleft()

            if board[x][y] == i:
                print(cnt)
                answer += cnt
                q = deque([[x, y, 0]])
                break

            for a, b in near:
                xi, yi = x + a, y + b
                if 0 <= xi < n and 0 <= yi < n:
                    q.append([xi, yi, cnt + 1])
                    # print('normal')
                elif xi == -1 and 0 <= yi < n:
                    q.append([n - 1, yi, cnt + 1])
                    # print('x-')
                elif xi == n and 0 <= yi < n:
                    q.append([0, yi, cnt + 1])
                    # print('x+')
                elif 0 <= xi < n and yi == -1:
                    q.append([xi, n - 1, cnt + 1])
                    # print('y-')
                elif 0 <= xi < n and yi == n:
                    q.append([xi, 0, cnt + 1])
                    # print('y+')

    return answer + total

n=4
board=[[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]
print(solution(n,board))
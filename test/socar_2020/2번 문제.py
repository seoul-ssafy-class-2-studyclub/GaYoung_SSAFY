import pprint
from collections import deque

drum = ['######','>#*###','####*#','#<#>>#','>#*#*<','######']

board = []
for i in drum:
    board.append(list(i))
pprint.pprint(board)

direct = ['#', '>', '<', '*']
direction = {'#':(1, 0), '>':(0, 1), '<':(0, -1), '*':(1, 0)}

N = len(drum)
answer = 0  # 구슬이 바닥에 떨어지는 위치 갯수
q = deque([])

for i in range(N):
    for j in range(N):
        if i == 0:
            q.append([i, j])

            cnt = 0  # '*'갯수 세기
            while q:
                print(q, cnt)
                x, y = q.popleft()

                if board[x][y] in direct:
                    xi, yi = x + direction[board[x][y]][0], y + direction[board[x][y]][1]

                    if 0 <= xi < N and 0 <= yi < N and board[xi][yi] in direct:
                        q.append([xi, yi])

                        if board[xi][yi] == '*':
                            cnt += 1

                            if cnt == 2:
                                break

                if x == N-1:
                    answer += 1
                    break

print(answer)


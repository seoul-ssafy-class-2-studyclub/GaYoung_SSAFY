N = int(input())
board = []
for n in range(N):
    board.append(list(map(int, input())))

stack = []
result_cnt = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt = 1
            stack.append(i)
            stack.append(j)
            board[i][j] = 0
            while stack:
                y = stack.pop()
                x = stack.pop()
                for idx in range(4):
                    xi = x + dx[idx]
                    yi = y + dy[idx]
                    if 0 <= xi < N and 0 <= yi < N:
                        if board[xi][yi] == 1:
                            board[xi][yi] = 0
                            stack.append(xi)
                            stack.append(yi)
                            cnt += 1
            result_cnt.append(cnt)
result_cnt.sort()
print(len(result_cnt))
for r in result_cnt:
    print(r)

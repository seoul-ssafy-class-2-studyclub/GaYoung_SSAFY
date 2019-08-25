dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = []
for n in range(N):
    board.append(list(map(int, input()))) 

result_cnt = []
for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            cnt = 1
            board[x][y] = -1
            queue = [x, y]
            while queue:
                x = queue.pop(0)
                y = queue.pop(0)
                for idx in range(4):
                    xi = x + dx[idx]
                    yi = y + dy[idx]
                    if 0 <= xi < N and 0 <= yi < N and board[xi][yi] == 1:
                        board[xi][yi] = -1
                        queue.append(xi)
                        queue.append(yi)
                        cnt += 1
            result_cnt.append(cnt)
            result = sorted(result_cnt)
print(len(result))

for r in result:
    print(r)

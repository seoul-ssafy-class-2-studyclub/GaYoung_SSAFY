n, m = map(int, input().split())  # 가로세로
end_x, end_y = map(int, input().split())

board = [[0] * (end_x+1) for _ in range(end_y+ 1)]
board[0][0] = 2
board[end_y][end_x] = 3
print(board)  # [[1, 0, 0], [0, 0, 2]]
near = [(0, 1), (1, 0)]
queue = []
visit = [[False] * (end_x+1) for _ in range(end_y+1)]
cnt = 0
for i in range(end_y+1):
    for j in range(end_x+1):
        if board[i][j] == 2:
            queue.append((i, j))
            visit[i][j] = True
            while queue:
                x, y = queue.pop(0)
                board[x][y] == 0
                for a, b in near:
                    xi, yi = (x + a, y + b)
                    if 0 <= xi < end_y + 1 and 0 <= yi < end_x + 1:
                        if board[xi][yi] == 0:
                            queue.append((xi, yi))
                            board[xi][yi] = 1
                        if board[xi][yi] == 3:
                            cnt += 1

print(cnt)
'''
dfs보다 bfs로 풀면 더 좋을듯
'''

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

near = [(0, -1), (0, 1), (1, 0), (-1, 0)]

result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt = 1
            q = [[i, j]]
            board[i][j] = 0

            while q:
                x, y = q.pop(0)
                for a, b in near:
                    xi, yi = x + a, y + b
                    if 0 <= xi < N and 0 <= yi < N:
                        if board[xi][yi] == 1:
                            cnt += 1
                            board[xi][yi] = 0
                            q.append((xi, yi))

            result.append(cnt)

result.sort()

print(len(result))
for i in result:
    print(i)


'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
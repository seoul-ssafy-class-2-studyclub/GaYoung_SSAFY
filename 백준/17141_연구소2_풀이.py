'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
5
'''

'''
[풀이방법]
1. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸
2. N, M = 가로/세로, 바이러스 갯수
3. 여러개 2 중에서 M개 선택 -> 조합!
4. 바이러스 위치가 결정되면, bfs돌리면서 몇초만에 퍼뜨리는지 check
5. 최소시간 구하기
6. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력
'''

# 바이러스 가능한 경우
result = []
def virus(arr, k):
    if len(arr) == M:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(can_virus)):
            virus(arr + [can_virus[idx]], idx)


mymin = 99999999999
def spread():
    cnt = 0
    while q:
        x, y = q.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < M:
                if new_board[xi][yi] == 0:
                    new_board[xi][yi] = 1
                    q.append((xi, yi))
                    cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
new_board = [row[:] for row in board]
near = [(-1, 0), (1, 0), (0, 1), (0, -1)]
safe = N * N - M

can_virus = []
# 바이러스 가능한 칸 찾기
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            can_virus.append([i, j])
            board[i][j] = 0
        elif board[i][j] == 1:
            safe -= 1

'''
board
[0, 0, 0, '-', '-']
[0, '-', '-', '-', '-']
[0, '-', '-', '-', '-']
[0, '-', '-', '-', '-']
[0, 0, 0, '-', '-']
'''

virus([], -1)
'''
result
[[[0, 0], [1, 5], [4, 3]], [[0, 0], [1, 5], [6, 0]], [[0, 0], [1, 5], [6, 6]], [[0, 0], [4, 3], [6, 0]], [[0, 0], [4, 3], [6, 6]], [[0, 0], [6, 0], [6, 6]], [[1, 5], [4, 3], [6, 0]], [[1, 5], [4, 3], [6, 6]], [[1, 5], [6, 0], [6, 6]], [[4, 3], [6, 0], [6, 6]]]
'''
cnt = 0
for r in result:
    q = r
    new_board = [row[:] for row in board]
    for s in range(M):
        a = r[s][0]
        b = r[s][1]
        new_board[a][b] = '*'  # 바이러스인 곳 표시
        for n in new_board:
            print(n)
        print(spread())
        print('====================================')
# print(board)
# print(spread(cnt))
        # print(a)
        # print('====================================')
        # break
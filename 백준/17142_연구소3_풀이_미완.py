'''
[풀이 방법]
0. 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.
1. 바이러스
   1-1. 활성상태: 상하좌우로 인접한 모든 빈 칸으로 동시에 복제(1초)
   1-2. 비활성상태: 처음 모든 바이러스
   1-3. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함
2. 벽: -, 비활성 바이러스: *, 활성 바이러스: 0, 빈 칸: 바이러스가 퍼지는 시간
3. 시간이 최소가 되는 방법은?
'''

'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
4
'''
from pprint import pprint

result = []
def can_virus(arr, k):
    if len(arr) == M:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(virus)):
            can_virus(arr + [virus[idx]], idx)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
safe = N * N

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
            board[i][j] = '*'
            safe -= 1
        elif board[i][j] == 1:
            safe -= 1

# pprint(board)
# print(safe)
for r in result:
    q = r[:]
    new_board = [row[:] for row in board]


'''
[풀이방법]
1. turn 함수 생성 -> (3,4,2), (4,2,1)연산 수행
2. mymin 지정해서 연산 수행이 끝날 때마다 최소값 구하기
  2-1. (3,4,2), (4,2,1)연산 수행 하면서 mymin 갱신
  2-2. (4,2,1), (3,4,2)연산 수행 하면서 mymin 갱신
'''

'''
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
'''

import itertools

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
do_ls = [list(map(int, input().split())) for _ in range(K)]

results = list(itertools.permutations(do_ls, K))
# print(result)  # [([3, 4, 2], [4, 2, 1]), ([4, 2, 1], [3, 4, 2])]

mymin = 9999999999999999999
for result in results:
    board1 = [row[:] for row in board]
    for res in result:
        r, c, s = res
        board2 = [row[:] for row in board1]
        r, c = r - 1, c - 1
        for k in range(s):
            # 위
            for i in range(r - k, r + k):
                board1[r - k][i + 1] = board2[][i + 1]
            # 아래
            for i in range():
                bd[k + 1][n] = board[k][n]
            # 오른쪽
            for i in range(n, mm - n):
                bd[nn - n][k + 1] = board[nn - n][k]
            # 왼쪽
            for i in range(mm - n, n, -1):
                bd[n][k - 1] = board[n][k]






print(mymin)
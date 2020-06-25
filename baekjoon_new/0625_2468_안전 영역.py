'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''

'''
[풀이방법]
1. 안전지역에서의 최대 높이(max_len)를 구한다.
2. 0부터 max_len까지 돌리면서 
   2-1. 매번 새로운 board를 가지고와서 해야함 -> deepcopy
   2-2. for i in range(max_len + 1)이면 l보다 작거나 같으면 0으로 표시
   2-3. bfs돌면서 1인 영역 갯수를 찾기 -> 안전영역 갯수(cnt)를 매번 구하면서 mymax에 갱신
'''
import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

temp = 0
for i in range(N):
    for j in range(N):
        if temp < board[i][j]:
            temp = board[i][j]

near = [(0, -1), (0, 1), (1, 0), (-1, 0)]
mymax = 0
for i in range(temp + 1):
    bd = copy.deepcopy(board)
    for n in range(N):
        for m in range(N):
            if bd[n][m] <= i:
                bd[n][m] = 0

    cnt = 0
    for n in range(N):
        for m in range(N):
            if bd[n][m] != 0:
                q = [[n, m]]
                cnt += 1
                bd[n][m] = 0

                while q:
                    x, y = q.pop(0)
                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < N and 0 <= yi < N and bd[xi][yi] != 0:
                            bd[xi][yi] = 0
                            q.append([xi, yi])

    if mymax < cnt:
        mymax = cnt

print(mymax)
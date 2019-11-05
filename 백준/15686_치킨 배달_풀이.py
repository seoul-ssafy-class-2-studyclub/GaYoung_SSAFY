'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
5
'''

'''
[풀이방법]
1. 치킨집 중 최대 M개를 구하고, 최소의 치킨거리 찾기
   1-1. 치킨집 최대 M개이므로, 1부터 M개까지 다 돌면서 최소거리 찾아야함
   1-2. 치킨집 조합 찾기 -> 1~M개
2. 0빈칸, 1집, 2치킨집
3. 치킨집은 치킨집대로, 집은 집대로 모아두고, 선택된 치킨집에서 집까지의 거리 구하기
'''
from copy import deepcopy

result = []
def chicken(arr, k):
    if len(arr) == M:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(store)):
            chicken(arr + [store[idx]], k + 1)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
new_board = deepcopy(board)

store = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            store.append([i, j])
        elif board[i][j] == 1:
            house.append([i, j])

chicken([], -1)
print(result)
'''
[result]
[[[1, 2], [2, 2], [4, 4]], [[1, 2], [4, 4], [4, 4]], [[2, 2], [2, 2], [4, 4]], [[2, 2], [4, 4], [4, 4]], [[4, 4], [2, 2], [4, 4]], [[4, 4], [4, 4], [4, 4]]]
'''

for r in result:
    for h in house:
        # 집의 좌표
        a = h[0]
        b = h[1]


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

store = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            store.append([i, j])
        elif board[i][j] == 1:
            house.append([i, j])

chicken([], -1)
'''
[result]
[[[1, 2], [2, 2], [4, 4]], [[1, 2], [4, 4], [4, 4]], [[2, 2], [2, 2], [4, 4]], [[2, 2], [4, 4], [4, 4]], [[4, 4], [2, 2], [4, 4]], [[4, 4], [4, 4], [4, 4]]]
'''

# 하나의 조합마다 집의 좌표로부터 치킨집거리를 구해서 최솟값 갱신하기
# 치킨집부터 집구하면 매번 M개만 구할 수 있음
# 우리가 구해야하는건 여러개의 집마다 치킨집 거리!!
answer = 99999999
for r in result:
    rs = 0  # 조합마다 갱신! (모든 집부터 치킨집 거리를 하나하나 더해서 최소값 찾기)
    for h in house:
        # 집의 좌표
        # a = h[0]
        # b = h[1]
        mymin = 999999  # 최소값으로 갱신 필요, 하나의 조합으로 하나의 집에서 치킨집M개중 고를 수 있음
        for k in r:
            # 치킨집 좌표
            # x = k[0]
            # y = k[1]
            # 하나의 집부터 치킨집 거리
            dis = abs(h[0] - k[0]) + abs(h[1] - k[1])
            if mymin > dis:
                mymin = dis
        # 그러면 모든 집부터 치킨집 거리를 알아야함
        rs += mymin
    if answer > rs:
        answer = rs

print(answer)

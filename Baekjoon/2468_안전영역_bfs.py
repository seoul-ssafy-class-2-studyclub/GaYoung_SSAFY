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
   2-1. 매번 처음 board를 가지고와서 해야함 -> deepcopy
   2-2. for l in range(max_len + 1)이면 높이가 l보다 크면 1, l보다 작거나 같으면 0으로 표시
   2-3. bfs돌면서 1인 영역 갯수를 찾기 -> 안전영역 갯수(cnt)를 매번 구하면서 mymax에 갱신
'''
from copy import deepcopy

N = int(input())
zone = [list(map(int, input().split())) for _ in range(N)]
zone_d = deepcopy(zone)

# 안전지역에서의 최대높이 구하기
max_h = 0
for i in range(N):
    for j in range(N):
        if max_h < zone[i][j]:
            max_h = zone[i][j]

def bfs():
    global cnt

    queue.append((i, j))
    zone[i][j] = 0
    while queue:
        x, y = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < N and zone[xi][yi] == 1:
                zone[xi][yi] = 0
                queue.append((xi, yi))
    return 1

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

queue = []
mymax = 0

# 0부터 max_len까지 돌리면서
for k in range(max_h + 1):
    zone = deepcopy(zone_d)
    for i in range(N):
        for j in range(N):
            if zone[i][j] > k:
                zone[i][j] = 1
            else:
                zone[i][j] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if zone[i][j] == 1:
                cnt += bfs()

    if mymax < cnt:
        mymax = cnt

print(mymax)

'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
'''
3
6 8 2
3 2 3
6 7 3
'''
from collections import deque

# def solution(N, road, K):
#     answer = 0
#     return answer

# def bfs():

# N = 5
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# K = 3

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

def check(maps, K, distance):

    first = 1
    queue = deque([first])
    distance[first] = 0  # 처음 출발한 도시의 거리는 0

    while queue:
        x = queue.popleft()
        for y in range(1,len(maps)):
            if maps[x][y] != 0:
                if distance[y] > distance[x] + maps[x][y] and distance[x] + maps[x][y] <= K:
                    distance[y] = distance[x] + maps[x][y]
                    queue.append(y)

    cnt = 0
    for dist in distance:
        if dist <= K:
            cnt += 1

    return cnt

'''
[[0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 2, 0],
 [0, 1, 0, 3, 0, 2],
 [0, 0, 3, 0, 0, 1],
 [0, 2, 0, 0, 0, 2],
 [0, 0, 2, 1, 2, 0]]
이런 형태를 만들고 싶다
'''

def makemap(N, road, K):
    maps = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # print(maps)
    '''
    [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0]]

    '''
    for start, end, w in road:
        # print(start,end,w)
        # 아무값이 들어있지 않으면
        if maps[start][end] == 0 and maps[end][start] == 0:
            maps[start][end] = w
            maps[end][start] = w
        # 중복된 값이 존재한다면
        else:
            if w < maps[start][end]:
                maps[start][end] = w
                maps[end][start] = w
    # return maps
    inf = float('inf')
    # distance: inf로 설정하고 도착 값이 inf보다 작으면 그 값을 대체 + 작으면 작을수록 대체
    distance = [inf for _ in range(N + 1)]

    return check(maps, K, distance)

print(makemap(N, road, K))
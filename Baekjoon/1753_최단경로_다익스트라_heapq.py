'''
[문제]
  시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을
'''

# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에

from pprint import pprint
from heapq import heappop, heappush

V, E = map(int, input().split())
start = int(input())

inf = float('inf')
adj = [[] for _ in range(V + 1)]

for _ in range(E):
    node1, node2, w = map(int, input().split())
    adj[node1].append((node2, w))
# print(adj)  # [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]


dis = [inf] * (V + 1)
dis[start] = 0

queue = []
heappush(queue, (0, start))

while queue:
    temp_d, temp_idx = heappop(queue)

    if temp_d > dis[temp_idx]:
        continue

    for item in adj[temp_idx]:
        target_idx, target_d = item
        temp = temp_d + target_d
        if temp < dis[target_idx]:
            dis[target_idx] = temp
            heappush(queue, (temp, target_idx))

for i in range(1, V + 1):
    if dis[i] == inf:
        print('INF')
    else:
        print(dis[i])
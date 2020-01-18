# 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 됨
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값 구하기

from heapq import heappush, heappop

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
# print(adj)
# [[], [(2, 2), (3, 3)], [(1, 2), (3, 2)], [(1, 3), (2, 2)]]

start, end = map(int, input().split())  # 1 3
visit = [False] * (N + 1)
visit[start] = True

q = [start]
mymax = 0
while q:
    pass


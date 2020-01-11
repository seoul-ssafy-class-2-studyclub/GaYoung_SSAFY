from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
print(adj)

for m in range(M):

def bfs(adj):
visit = [False] * (M + 1)
q = [1]
t = 0
while q:
node = q.pop(0)
if not visit[node]:
visit[node] = True
t += time
q.extend(adj[node])
return t

N, M, X = map(int, input().split())
adj = [[] for _ in range(M + 1)]
for m in range(M):
start, end, time = list(map(int, input().split()))
adj[start].append(end)

print(bfs(adj))
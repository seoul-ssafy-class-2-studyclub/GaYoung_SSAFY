# bfs방법

def bfs(adj):
    visit = [False] * (comp + 1)
    q = [1]
    cnt = 0
    while q:
        node = q.pop(0)
        if not visit[node]:
            visit[node] = True
            cnt += 1
            q.extend(adj[node])
    return cnt - 1


comp = int(input())
N = int(input())
adj = [[] for _ in range(comp + 1)]

for n in range(N):
    data = list(map(int, input().split()))
    adj[data[0]].append(data[1])
    adj[data[1]].append(data[0])

print(bfs(adj))


# dfs 방법
def dfs(adj):
    visit = [False] * (comp + 1)
    stack = [1]
    cnt = 0
    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node] = True
            cnt += 1
            stack.extend(adj[node])
    return cnt - 1

comp = int(input())
N = int(input())
adj = [[] for _ in range(comp + 1)]
for n in range(N):
    data = list(map(int, input().split()))
    adj[data[0]].append(data[1])
    adj[data[1]].append(data[0])

print(dfs(adj))
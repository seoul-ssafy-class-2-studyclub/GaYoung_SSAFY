from heapq import heappop, heappush

N = int(input())
M = int(input())


adj = [{} for _ in range(N)]
visit = [False] * N
w_list = [99999999999999 for _ in range(N)]
w_list[0] = 0

for m in range(M):
    n1, n2, w = map(int, input().split())
    adj[n1-1][n2-1] = w
    adj[n2-1][n1-1] = w

q = []
heappush(q, (0, 0))
while q:
    temp_w, temp_n = heappop(q)
    visit[temp_n] = True
    for key, val in adj[temp_n].items():
        if visit[key] == False and w_list[key] > val:
            w_list[key] = val
            heappush(q, (w_list[key], key))

print(sum(w_list))
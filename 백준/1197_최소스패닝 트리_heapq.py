from heapq import heappush, heappop

V, E = map(int, input().split())

adj = [{} for _ in range(V)]
visit = [False] * (V)
w_list = [99999999999999 for _ in range(V)]
w_list[0] = 0

for e in range(E):
    n1, n2, w = map(int, input().split())
    adj[n1-1][n2-1] = w
    adj[n2-1][n1-1] = w

# print(adj)
q = []
heappush(q, (0, 0))
while q:
    temp_w, temp_n = heappop(q)
    visit[temp_n] = True
    for key, val in adj[temp_n].items():
        if visit[key] == False and w_list[key] > val:
            w_list[key] = val
            heappush(q, (w_list[key], key))
#
print(sum(w_list))
from heapq import heappush, heappop

V, E = map(int, input().split())

inf = float('inf')
# print(inf)
dijkstra = [inf] * V

start = int(input()) - 1
dijkstra[start] = 0
# print(dijkstra)
adj = [{} for _ in range(V)]
visit = [False] * V

for e in range(E):
    n1, n2, w = map(int, input().split())
    if n2 - 1 in adj[n1 - 1]:  # 값이 존재하면
        if adj[n1 - 1][n2 - 1] > w:  # 기존 값보다 작을때만 갱신
            adj[n1 - 1][n2 - 1] = w
    else:  # 기존에 값이 존재하지 않는다면
        adj[n1 - 1][n2 - 1] = w  # 값을 넣어줌
# print(adj)

q = []
heappush(q, (0, start))
while q:
    temp_w, temp_n = heappop(q)
    #
    # if visit[temp_n] == False:
    #     visit[temp_n] = True

    for key, val in adj[temp_n].items():
        if visit[key] == False:
            if dijkstra[key] > temp_w + val:
                dijkstra[key] = temp_w + val
                heappush(q, (dijkstra[key], key))

            visit[temp_n] = True

for i in range(V):
    if dijkstra[i] == inf:
        print('INF')
    else:
        print(dijkstra[i])

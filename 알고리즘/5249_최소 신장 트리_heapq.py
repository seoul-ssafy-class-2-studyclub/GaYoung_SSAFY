# heapq, 인접리스트
from heapq import heappush, heappop
for t in range(int(input())):
    V, E = map(int, input().split())
    adj = [{} for _ in range(V + 1)]  # 인접 리스트
    for e in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    # print(adj)

    q = []
    heappush(q, (0, 0))  # 앞에 있는 것이 가중치, 뒤에 있는 것이 노드
    w_list = [1e9 for _ in range(V + 1)]
    w_list[0] = 0  # start점은 가중치를 0으로 두고 시작

    visit = [False for _ in range(V + 1)]

    while q:
        temp_w, temp_n = heappop(q)
        visit[temp_n] = True
        for key, val in adj[temp_n].items():
            if visit[key] == False and w_list[key] > val:
                w_list[key] = val
                heappush(q, (w_list[key], key))

    print('#{} {}'.format(t+1, sum(w_list)))
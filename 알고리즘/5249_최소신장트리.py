V, E = map(int, input().split())

inf = float('inf')
w_list = [[inf] * (V + 1) for _ in range(V + 1)]

visit = [True] + [False] * V

for _ in range(E):
    node1, node2, w = map(int, input().split())
    w_list[node1][node2] = w
    w_list[node2][node1] = w

cnt = 0
sum_w = 0
while cnt < V:
    min_w = 11

    for i in range(V + 1):
        if visit[i]:
            for j in range(V + 1):
                if visit[j] == False and min_w > w_list[i][j]:
                    min_w = w_list[i][j]
                    start_node = i
                    end_node = j

    visit[end_node] = True
    sum_w += w_list[start_node][end_node]
    cnt += 1
print(sum_w)

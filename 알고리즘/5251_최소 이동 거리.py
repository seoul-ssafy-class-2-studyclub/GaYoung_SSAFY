from pprint import pprint

N, E = map(int, input().split())

inf = 100
arr = [0] + [inf for _ in range(N)]

visit = [False] * (N + 1)
adj_list = [[inf] * (N + 1) for _ in range(N + 1)]

for _ in range(E):
    node1, node2, w = map(int, input().split())
    adj_list[node1][node2] = w  # 일방통행

idx = 0
while True:
    min_value = inf

    for i in range(1, N + 1):
        if visit[i] == False and min_value > arr[i]:
            min_value = arr[i]
            idx = i

    if idx == N:
        break

    else:
        visit[idx] = True
        for i in range(1, N + 1):
            if visit[i] == False:
                arr[i] = min(arr[i], arr[idx] + adj_list[idx][i])

print(min_value)

for t in range(int(input())):
    V, E = map(int, input().split())

    w_list = [[1e9] * (V + 1) for _ in range(V + 1)]
    visit = [True] + [False] * V

    for e in range(E):
        n1, n2, w = map(int, input().split())
        w_list[n1][n2] = w
        w_list[n2][n1] = w

    cnt = 0
    sum_w = 0
    while cnt < V:
        min_w = 11

        for i in range(V + 1):
            if visit[i]:
                for j in range(V + 1):
                    if visit[j] == False and min_w > w_list[i][j]:
                        min_w = w_list[i][j]
                        start_n = i
                        end_n = j
        visit[end_n] = True
        sum_w += w_list[start_n][end_n]
        cnt += 1

    print(sum_w)
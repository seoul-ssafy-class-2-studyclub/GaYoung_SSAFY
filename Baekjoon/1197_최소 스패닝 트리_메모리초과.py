V, E = map(int, input().split())

w_list = [[1e9] * V for _ in range(V)]
for e in range(E):
    n1, n2, w = map(int, input().split())
    w_list[n1-1][n2-1] = w
    w_list[n2-1][n1-1] = w

visit = [True] + [False] * (V-1)

# print(sum_w)

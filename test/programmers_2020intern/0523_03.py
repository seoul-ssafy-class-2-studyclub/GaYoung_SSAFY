import pprint

def solution(total_sp, skills):
    N = len(skills) + 1

    up = [0 for _ in range(N)]
    down = [[0 for _ in range(N)] for _ in range(N)]

    for sk in skills:
        if sk[1]:
            down[sk[0] - 1][sk[1] - 1] = 1

    for sk in skills:
        if sk[0]:
            up[sk[0] - 1] = 1

    check = [0 for _ in range(N)]
    for i in range(len(down)):
        for j in range(i, len(down)):
            if down[i][j] == 1:
                check[i] += 1
                check[j] += 1

    for u in range(len(up)):
        for d in range(len(down)):
            if down[u][d] == 1 and up[u] == 1:
                if up[d] == 1:  # 3인 경우
                    check[d] -= 1
                    up[u] += check[d]
                    check[u] -= 1
                    check[u] += check[d]
                else:  # 2인 경우
                    continue

    res = total_sp // sum(check)
    # print(res)
    check = [i * res for i in check]
    # print(check)

    return check


total_sp = 121
skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]


# up
# [1, 0, 1, 0, 0, 0, 0]
# down
# [[0, 1, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]

def solution(routes):

    routes = sorted(routes, reverse=True)

    check = [0] * len(routes)
    cnt = 0
    camera = 0
    for i in range(len(routes)):
        if check[i] == 0:
            camera = routes[i][0]
            cnt += 1

        for j in range(i + 1, len(routes)):
            if routes[j][0] <= camera <= routes[j][1]:
                check[j] = 1

    # print(cnt)
    return cnt

routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

# [[-5, -3], [-14, -5], [-18, -13], [-20, 15]]

def solution(routes):
    routes = sorted(routes, reverse=True)

    cnt = 0
    camera = 0
    visit = [0] * len(routes)
    for i in range(len(routes)):
        if visit[i] == 0:
            camera = routes[i][0]
            cnt += 1

        for j in range(i+1, len(routes)):
            if routes[j][0] <= camera <= routes[j][1]:
                visit[j] = 1

    # print(cnt)
    return cnt

print(solution(routes))
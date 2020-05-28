
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]



def where(computers, visit, start):
    stack = [start]
    while stack:
        i = stack.pop()
        if visit[i] == 0:
            visit[i] = 1
        for j in range(0, len(computers)):
            if computers[i][j] == 1 and visit[j] == 0:
                visit[j] = 1
                stack.append(j)


def solution(n, computers):
    cnt = 0
    visit = [0 for _ in range(n)]

    for i in range(len(visit)):
        if visit[i] == 0:
            where(computers, visit, i)
            cnt += 1
    # print(cnt)

    return cnt

print(solution(n, computers))



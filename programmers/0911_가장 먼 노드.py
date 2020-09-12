n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque


def solution(n, edge):
    visit = [0] * (n + 1)

    graph = {i: [] for i in range(1, n + 1)}
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    q = deque([1])
    visit[1] = 1
    mymax = 0
    while q:
        x = q.popleft()
        for j in graph[x]:
            if visit[j] == 0:
                visit[j] = visit[x] + 1
                mymax = visit[j]
                q.append(j)

    return visit.count(mymax)
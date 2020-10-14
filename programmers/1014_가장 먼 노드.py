from collections import deque

def solution(n, edge):
    line = {i: [] for i in range(1, n+1)}
    for start, end in edge:
        line[start].append(end)
        line[end].append(start)

    visit = [0] * (n+1)
    q = deque([1])
    visit[1] = 1
    mymax = 0
    while q:
        x = q.popleft()

        for i in line[x]:
            if not visit[i]:
                q.append(i)
                visit[i] = visit[x] + 1
                mymax = visit[i]

    return visit.count(mymax)


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

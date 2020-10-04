from collections import deque

def solution(n, computers):
    q = deque()
    visit = [0] * n
    cnt = 0
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            q.append(i)

            while q:
                x = q.popleft()
                print(x)
                for y in range(n):
                    if computers[x][y] == 1 and visit[y] == 0:
                        print(y)
                        visit[y] = 1
                        q.append(y)

            cnt += 1

    # print(cnt)
    return cnt

n = 3
computeres = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# n = 3
# computeres = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]




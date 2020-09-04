from collections import deque

def solution(n, computers):
    visit = [0] * n
    cnt = 0
    q = deque()
    for i in range(n):
        if visit[i] == 0:
            q.append(i)
            visit[i] = 1

            # bfs문에 들어간 횟수 = 네트워크 갯수
            while q:
                x = q.popleft()
                for j in range(n):
                    if computers[x][j] == 1 and visit[j] == 0:
                        visit[j] = 1
                        q.append(j)

            cnt += 1

    return cnt


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


'''
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
답 : 2 -> why? 1,2가 하나의 네트워크, 3이 하나의 네트워크


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
답 : 1 -> why? 1,2,3이 하나의 네트워크
'''


import heapq

def solution(jobs):
    answer = 0
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
n = len(jobs)
time, end, q = 0, -1, []
cnt = 0
answer = 0
while cnt < n:
    for i in jobs:
        if end < i[0] <= time:  # time = 기존 코드의 start
            answer += (time - i[0])
            heapq.heappush(q, i[1])
            print(q)
    if len(q) > 0:
        # 가장 빨리 끝나는 프로세스가 끝날 때까지는 queue에 있는 프로세스 전부 대기시간
        answer += len(q) * q[0]
        end = time
        time += heapq.heappop(q)
        cnt += 1

    else:
        time += 1  # q에 아무것도 없으므로 시간 += 1
    print(q)
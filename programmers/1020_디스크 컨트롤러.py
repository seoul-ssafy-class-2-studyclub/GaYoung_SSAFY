def solution(jobs):
    answer = 0
    return answer


jobs = [[0, 3], [1, 9], [2, 6]]

import heapq

last = -1
now = 0
answer = 0  # 값의 합
wait = []
n = len(jobs)
count = 0
while count < n:
    for job in jobs:
        if last < job[0] <= now:
            answer += (now - job[0])
            heapq.heappush(wait, job[1])

    if len(wait) > 0:
        pass

    print(wait)
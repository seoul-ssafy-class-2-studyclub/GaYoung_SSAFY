scoville = [1, 2, 3, 9, 10, 12]
K = 9

import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)  # 리스트를 힙구조로 만들어야한다.
    while True:
        # print(scoville)
        if scoville[0] >= K:
            return cnt

        if len(scoville) == 1 and scoville[0] < K:
            return -1

        if len(scoville) >= 2:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            temp = first + second * 2
            cnt += 1
            heapq.heappush(scoville, temp)


print(solution(scoville, K))

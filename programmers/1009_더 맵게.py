import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # heapq를 사용하기 위해서는 heapify로 정렬해주기

    cnt = 0
    while True:

        if scoville[0] >= K:
            return cnt

        if len(scoville) == 1 and scoville[0] < K:
            return -1

        elif len(scoville) >= 2:
            cnt += 1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            val = first + second * 2
            heapq.heappush(scoville, val)



scoville = [1, 2, 3, 9, 10, 12]
K = 9999999999999999999999999999999

# scoville = [1, 2]
# K = 3
print(solution(scoville, K))
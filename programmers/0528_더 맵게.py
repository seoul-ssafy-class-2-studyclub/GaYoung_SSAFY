scoville = [1, 2, 3, 9, 10, 12]
K = 7


################ 내풀이 ##################
import heapq

def solution(scoville, K):
    ls = []
    for scov in scoville:
        heapq.heappush(ls, scov)

    cnt = 0
    while len(ls) > 0:
        # print(ls)
        if ls[0] >= K:
            return cnt

        # len같은 계산 시간많이든다!! -> first는 미리 빼버리고, ls != []일때, second꺼내기
        first = heapq.heappop(ls)
        if ls != []:
            second = heapq.heappop(ls)
            res = first + second * 2
            heapq.heappush(ls, res)
        cnt += 1

    return -1

print(solution(scoville,K))




################ 빠름!!! ##################
import heapq as hq

def solution2(scoville, K):

    hq.heapify(scoville)
    # print(scoville)  # [1, 2, 3, 9, 10, 12]
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer

print(solution2(scoville,K))
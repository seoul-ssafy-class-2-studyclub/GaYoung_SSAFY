# 정확성 성공, 효율성 실패
def solution(n, works):
    
    if n >= sum(works):
        return 0

    while n:
        works[works.index(max(works))] -= 1
        n -= 1

    answer = 0
    for i in works:
        answer += i ** 2
    # print(answer)

    return answer

# n = 3
# works = [1, 1]

n = 4
works = [4, 3, 3]

# n = 1
# works = [2, 1, 2]


import heapq

# 정확성 성공, 효율성 성공
def solution1(n, works):
    
    if n >= sum(works):
        return 0

    heap = []
    for value in works:
        heapq.heappush(heap,(-value,value))

    while n:
        x = heapq.heappop(heap)
        value = x[1] - 1
        heapq.heappush(heap, (-value, value))
        n -= 1

    answer = 0
    for i in heap:
        answer += i[1] ** 2

    return answer

print(solution1(n,works))
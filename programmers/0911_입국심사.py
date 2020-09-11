n = 6
times = [7, 10]

'''
1. 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
   + 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다. -> 이분탐색
2. start, end, mid 기준 -> end=모든사람이 심사끝나는 최대 시간, mid=인원
'''

def solution(n, times):
    left, right = 0, max(times) * n

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        people = 0

        # mid시간동안 얼마나 많은 사람들을 심사할 수 있는가
        for i in times:
            people += mid // i
        # 0 ~ mid(=35) 35분동안 5명, 3명 심사. -> 8명 심사

        if people < n:  # 8명 심사가능인데 우리는 6명만 심사하면 된다. 그렇기 때문에 end점을 줄인다.
            left = mid + 1

        else:
            right = mid - 1
            answer = mid

    # print(answer)
    return answer
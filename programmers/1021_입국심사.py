# n = 6
# times = [7, 10]
# n = 1000000000
# times = [1, 1000000000, 1,000000000]  # return 1000000000
n = 10
times = [1, 5]

'''
[로직]
1. 심사 가능 시간은 0 ~ 최대로 걸리는 시간 * 사람명수
2. 중간 값들을 구하면서 사람이 몇명 심사받을 수 있는지 확인
'''

def solution(n, times):
    left, right = 0, max(times) * n

    answer = 0
    while left <= right:
        # print(left, right)
        mid = (left + right) // 2
        people = 0

        for i in times:
            people += mid // i  # 0 ~ mid까지 심사


        if people < n:
            left = mid + 1

        else:
            right = mid - 1
            answer = mid
        # if people > n:
        #     right = mid
        #
        # elif people < n:
        #     left = mid
        #
        # elif people == n:  # people == n을 만족시키는 mid의 값은 여러개가 될 수 있다.
        #     return mid
    return answer


print(solution(n, times))
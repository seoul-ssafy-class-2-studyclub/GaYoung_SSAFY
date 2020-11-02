def solution(nums):
    answer = 0
    length = len(nums) // 2
    ls = list(set(nums))

    for i in ls:
        if answer < length:
            answer += 1

    # print(answer)
    return answer

nums = [3,1,2,3]
# nums = [3,3,3,2,2,4]
# nums = [3,3,3,2,2,2]


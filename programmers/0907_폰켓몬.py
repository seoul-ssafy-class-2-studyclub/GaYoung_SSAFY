def solution(nums):
    poket = {}
    get = len(nums) // 2
    for i in range(len(nums)):
        if nums[i] in poket:
            poket[nums[i]] += 1

        else:
            poket[nums[i]] = 1

    if get >= len(poket):
        get = len(poket)

    # print(get)
    return get


# nums = [3,1,2,3]
# nums = [3,3,3,2,2,4]
nums = [3,3,3,2,2,2]



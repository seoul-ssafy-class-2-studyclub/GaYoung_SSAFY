# # 순열 함수 만들기 -> 시간초과
# def solution(nums):
#     result = []
#     def comb(arr, k):
#         for n in range(len(nums) + 1):
#             if len(arr) == 3:
#                 if arr not in result:
#                     result.append(arr)
#
#             else:
#                 for idx in range(k + 1, len(nums)):
#                     comb(arr + [nums[idx]], idx)
#
#     comb([], -1)
#
#     def check(a, b, c):
#         total = a + b + c
#         print(total)
#         for i in range(2, total):
#             if total % i == 0:
#                 return False
#         return True
#
#     # print(result)
#     cnt = 0
#     for r in result:
#         if check(r[0], r[1], r[2]):
#             cnt += 1
#
#     return cnt

# print(solution([1,2,3,4]))


def solution(nums):
    def check(a, b, c):
        total = a + b + c
        for i in range(2, total):
            if total % i == 0:
                return False
        return True

    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if check(nums[i],nums[j],nums[k]):
                    cnt += 1

    return cnt

print(solution([1,2,3,4]))
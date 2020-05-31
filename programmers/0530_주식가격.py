# 방법1. pop()사용하니 시간 초과
# def solution(prices):
#     cnt = 0
#     answer = []
#     while prices != []:
#         price = prices.pop(0)
#
#         if (price - 1) not in prices:
#             cnt = len(prices)
#         else:
#             for i in range(len(prices)):
#                 if prices[i] == (price - 1):
#                     cnt = i + 1
#             # ans = len(prices)
#             # break
#         answer.append(cnt)
#
#     # print(answer)
#
#     return answer




prices = [1, 2, 3, 2, 3]

def solution(prices):
    ans = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                ans[i] += 1

            else:
                break

    # print(ans)

    return ans


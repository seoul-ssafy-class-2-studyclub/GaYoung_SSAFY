def solution(prices):
    len_prices = len(prices)
    answer = [0] * len_prices

    for i in range(len_prices - 1):
        for j in range(i, len_prices - 1):
            if prices[i] <= prices[j]:
                answer[i] += 1

            else:
                break

    # print(answer)

    return answer


prices = [1, 2, 3, 2, 3, 3]

print(solution(prices))
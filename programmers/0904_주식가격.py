def solution(prices):
    answer = [0] * len(prices)

    '''
    prices = [1, 2, 3, 2, 3]이면 [4, 3, 1, 1, 0]이다.
    prices[2]의 경우 3 -> 2로 갈때 1초가 걸리니까 1초간은 가격이 떨어지지 않은 것이다.
    그래서 for i in range(len(prices)-1): for j in range(i, len(prices)-1):이고, 
    이때, len(prices)하면 [5, 4, 1, 2, 1]이 됨
    answer.append(cnt)하면 마지막 가격은 무조건 0초이기때문에 answer.append(0)을 무조건 해야함
    answer = [0] * len(prices)을 두고 더하면 더 빠르다.
    '''
    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break

    return answer


prices = [1, 2, 3, 2, 3]
# prices = [1, 2, 3, 2, 3, 3]

print(solution(prices))

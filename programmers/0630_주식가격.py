def solution1(prices):
    cnt = [0 for _ in range(len(prices))]

    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt[i] += 1

            else:
                cnt[i] += 1
                break
            print(cnt)
    return cnt


def solution(prices):
    answer = [0]* len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: # 뒤에 수가 같거나 크면 계속 더해라
                answer[i] += 1
                print(i, j, answer)
            else: # 이전 것보다 숫자가 작아지면 떨어지면 거기 까지 더한 수를 반환하라
                if answer[i] == 0:
                    answer[i] = 1
                    print(i, j, answer)
                break

    return answer

prices = [ 1, 2, 3, 2, 3, 1 ]
print(solution(prices))
print('--------------------')
print(solution1(prices))

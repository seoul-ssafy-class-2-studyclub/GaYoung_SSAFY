def solution(money, expected, actual):
    start_money = 100
    for i in range(len(expected)):
        if money > 0:
            if expected[i] == actual[i]:
                money += start_money
                start_money = 100

            else:
                money -= start_money
                val = start_money * 2
                if val <= money:
                    start_money *= 2
                else:
                    start_money = money

        else:
            break

        # print(money)

    return money
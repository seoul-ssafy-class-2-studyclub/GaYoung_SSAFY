import heapq

# def solution(stock, dates, supplies, k):
#     answer = 0
#     return answer

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30

cnt = 0
ls = []
day = 0
while stock > 0:
    stock -= 1
    day += 1

    print('stock')
    print(stock)
    print('day')
    print(day)
    print('-1--------------------------------------------')

    for i in range(len(dates)):
        if day >= dates[i]:
            ls.append(supplies[i])
            print('ls')
            print(ls)
            print('-2--------------------------------------------')

        elif day + stock < k:
            plus = dates[i] - day
            print('plus')
            print(plus)
            print('-3--------------------------------------------')
            
            if plus < stock:
                day += plus
                stock -= plus

            print('stock')
            print(stock)
            print('day')
            print(day)
            print('--cycle-------------------------------------------')





print(cnt)
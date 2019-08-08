for t in range(int(input())):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_count = [0, 0, 0, 0, 0, 0, 0, 0]    
    data = int(input())

    for i in range(len(money)):
        while data - money[i] >= 0:
            money_count[i] += 1
            data -= money[i]
        
    money_count = list(map(str, money_count))
    print('#{0}'.format(t+1))
    print(' '.join(money_count))
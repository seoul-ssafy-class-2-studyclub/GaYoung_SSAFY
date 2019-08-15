def my_max(x):
    my_value = x[0]
    for num in x:
        if my_value < num:
            my_value = num
    return my_value
    
for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    result = []

    for score in range(1, 101):
        result += [data.count(score)]
    
    for score in range(100, -1, -1):
        if data.count(score) == my_max(result):
            answer = score
            break

    print('#{} {}'.format(N, answer))
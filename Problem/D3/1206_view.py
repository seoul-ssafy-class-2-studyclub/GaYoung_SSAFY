def my_min(x):
    my_value = x[0]
    for num in x:
        if my_value > num:
            my_value = num
    return my_value

for t in range(10):
    n = int(input())
    data = list(map(int, input().split()))
    result = []
    for i in range(2, n-2):
        if data[i] - data[i-2] > 0 and data[i] - data[i-1] > 0 and data[i] - data[i+1] > 0 and data[i] - data[i+2] > 0:
            result += [[data[i] - data[i-2], data[i] - data[i-1], data[i] - data[i+1], data[i] - data[i+2]]]

    total = 0
    for r in result:
        total += my_min(r)
    print('#{0} {1}'.format(t+1, total))

def my_min(x):
    my_value = x[0]
    for num in x:
        if my_value > num:
            my_value = num
    return my_value

def my_max(x):
    my_value = x[0]
    for num in x:
        if my_value < num:
            my_value = num
    return my_value

def my_sum(x):
    my_value = 0
    for num in x:
        my_value += num
    return my_value

for t in range(int(input())):
    N, M = list(map(int, input().split()))
    data = list(map(int, input().split()))
    result = []
    for i in range(len(data)-M+1):  # 0~9
        result += [my_sum(data[i:i+M])]
    ans = my_max(result) - my_min(result)
    print('#{0} {1}'.format(t+1, ans))
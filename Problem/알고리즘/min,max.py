# min 함수
def my_min(x):
    my_value = x[0]
    for num in x:
        if my_value > num:
            my_value = num
    return my_value

# max 함수
def my_max(x):
    my_value = x[0]
    for num in x:
        if my_value < num:
            my_value = num
    return my_value

for t in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    result = my_max(data) - my_min(data)
    print('#{0} {1}'.format(t+1, result))
    
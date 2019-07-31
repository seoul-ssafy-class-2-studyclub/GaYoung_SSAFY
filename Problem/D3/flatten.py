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

def find_index(x, arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

for t in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    for n in range(N):
        max_index = data.index(my_max(data))
        min_index = data.index(my_min(data))

        data[max_index] -= 1
        data[min_index] += 1

    print('#{0} {1}'.format(t+1, my_max(data)-my_min(data)))
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left = []
    right = []
    equal = []
    pivot = arr[len(arr) // 2]
    for x in arr:
        if x > pivot:
            right.append(x)
        elif x < pivot:
            left.append(x)
        else:
            equal.append(x)
    return quick_sort(left) + equal + quick_sort(right)

def my_sum(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
    return result


def my_mean(arr):
    result = my_sum(arr) / len(arr)
    return result


for t in range(int(input())):
    data = list(map(int, input().split()))
    result = quick_sort(data)[1:len(quick_sort(data))-1]
    print('#{0} {1}'.format(t+1, round(my_mean(result))))
    
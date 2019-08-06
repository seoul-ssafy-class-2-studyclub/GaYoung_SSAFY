def quick_sort(arr):  
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    equal = []
    pivot = arr[0]
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)
    return quick_sort(left) + equal + quick_sort(right)

for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    print('#{0}'.format(t+1), end=' ')
    print(' '.join(map(str, quick_sort(data))))

def quick(arr):  # 제자리에서 수행됨

    if len(arr) <= 1:
        return arr

    '''
    만약 left가 진행되다가 [0, 1, 0, 7, 3]이면 0을 기준으로했을 때, arr가 비어있을 수 있다.
    따라서 if문에서 걸러준 다음에 pivot = arr[0]을 적어줘야함.
    left = equal = right = []는 위에 적어도 ok
    '''

    pivot = arr[0]
    left = []
    equal = []
    right = []

    for num in arr:
        if num < pivot:
            left += [num]
        elif num > pivot:
            right += [num]
        else:
            equal += [num]

    return quick(left) + equal + quick(right)  # 정복
        # 모두가 리스트이므로 그냥 더해주면 하나의 리스트로 나옴


for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    result = quick(data)
    print('#{} {}'.format(t+1, result[N//2]))
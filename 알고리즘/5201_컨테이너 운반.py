for t in range(int(input())):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())))  # [1, 3, 5]
    truck = sorted(list(map(int, input().split())))  # [3, 8]
    result = 0


    while truck:
        ti = truck.pop()
        while container:
            ci = container.pop()
            if ti >= ci:
                result += ci
                break

    print('#{} {}'.format(t + 1, result))

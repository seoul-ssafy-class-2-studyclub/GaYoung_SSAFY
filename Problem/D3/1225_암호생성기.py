for t in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    i = 1
    while not (0 in data):
        a = data.pop(0) - i
        if a <= 0:
            a = 0
        data.append(a)
        i += 1
        if i > 5:
            i = 1
    print(data)

result = ' '.join(map(str, data))
print('#{} {}'.format(N, result))
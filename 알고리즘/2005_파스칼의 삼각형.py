for t in range(int(input())):
    N = int(input())
    result = []

    for i in range(N):
        data = [0] * (i + 1)
        data[0] = data[-1] = 1
        result.append(data)

    for k in range(2, N):
        for j in range(1, len(result[k]) - 1):
            result[k][j] = result[k - 1][j - 1] + result[k - 1][j]

    print('#{}'.format(t+1))
    for n in result:
        print(' '.join(map(str, n)))
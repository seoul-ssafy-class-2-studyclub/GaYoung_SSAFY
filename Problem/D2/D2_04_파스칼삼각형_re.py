for t in range(int(input())):
    N = int(input())
    result = []

    for n in range(N):
        data = [0] * (n + 1)
        data[0] = data[-1] = 1
        result.append(data)

    for i in range(2, N):
        for j in range(1, len(result[i]) - 1):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    print('#{}'.format(t + 1))
    for r in result:
        print(' '.join(map(str, r)))  # join은 str만 사용 가능
        # join은 리스트안의 str을 빼낼 때 사용
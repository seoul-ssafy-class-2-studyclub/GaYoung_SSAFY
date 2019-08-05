for t in range(int(input())):
    N = int(input())
    result = []
    for k in range(N):
        for i in range(N):
            data = [0] * (i+1)
            # print(data)
            data[0] = data[-1] = 1
            data[k][i+1] += data[k-1][i] + data[k-1][i-1]
            result.append(data)

print(result)
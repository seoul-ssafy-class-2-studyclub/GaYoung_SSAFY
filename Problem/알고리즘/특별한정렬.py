# 작은 수부터 큰수로 정렬 
for t in range(int(input())):
    result = []
    N = int(input())
    data = list(map(int, input().split()))

    for k in range(len(data)-1):
        for i in range(len(data)-k-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

# N이 짝수인 경우 특별 정렬
    if N % 2 == 0:
        for i in range(N-1, N//2-1, -1):
            result.append(data[i])
        for j in range(N // 2):
            result.insert(2*j+1, data[j])

# N이 홀수인 경우 특별 정렬
    else:
        for i in range(N-1, N//2-1, -1):
            result.append(data[i])
        for j in range(N // 2):
            result.insert(2*j+1, data[j])

# 결과값 프린트
    print('#{0}'.format(t+1), end=' ')
    for k in range(10):
        if k < 9:
            print(result[k], end=' ')
        else:
            print(result[k])
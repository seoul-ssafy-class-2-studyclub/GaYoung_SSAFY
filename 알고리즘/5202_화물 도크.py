for t in range(int(input())):
    N = int(input())
    data = []
    for n in range(N):
        data.append(list(map(int, input().split())))
    data.sort(key=lambda x:x[1])
    cnt = 1
    end = data[0][1]

    for i in range(1, N):
        start = data[i][0]
        if start >= end:
            end = data[i][1]
            cnt += 1

    print('#{} {}'.format(t + 1, cnt))

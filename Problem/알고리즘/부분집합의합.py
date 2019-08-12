a = [i for i in range(1, 13)]


for t in range(int(input())):
    N, K = map(int, input().split())  # 3, 6
    count = 0
    for i in range(1 << 12):  # i = 000, 001, ,,, 111
        result = []
        for j in range(len(a)):
            if i & (1 << j):  # 참이라면
                result += [a[j]]
            if len(result) > N or sum(result) > K:
                break
        if len(result) == N and sum(result) == K:
            count += 1
    print('#{0} {1}'.format(t+1, count))

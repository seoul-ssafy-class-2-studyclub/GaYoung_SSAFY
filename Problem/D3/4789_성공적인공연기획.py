for t in range(int(input())):
    data = list(map(int, input()))
    count = 0
    for i in range(1, len(data)+1):
        if sum(data[:i]) < i:
            data[i-1] += 1
            count += 1
    print('#{0} {1}'.format(t+1, count))
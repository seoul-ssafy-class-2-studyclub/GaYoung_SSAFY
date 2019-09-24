def bus(idx, k, cnt):
    global mymin

    if idx >= N - 1:
        if mymin > cnt - 1:
            mymin = cnt - 1
        return

    if mymin < cnt:
        return

    for i in range(1, k + 1):
        if idx + i <= N - 1:
            bus(idx + i, data[idx+i], cnt + 1)



for t in range(int(input())):
    data = list(map(int, input().split()))
    N = data.pop(0)
    cnt = 0
    k = data[0]
    data.append(0)
    mymin = 999999999

    bus(0, k, 0)

    print('#{} {}'.format(t+1, mymin))
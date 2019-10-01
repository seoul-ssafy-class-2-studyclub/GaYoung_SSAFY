def bus(idx, k, cnt):
    global mymin

    if idx >= N - 1:
        # idx는 0~4까지 이므로 4보다 크거나같으면(마지막idx보다 크거나 같으면 그때의 cnt 구하기)
        if mymin > cnt - 1:
            mymin = cnt - 1
        return

    if mymin < cnt:
        return

    for i in range(1, k + 1):
        if idx + i <= N - 1:
            bus(idx + i, data[idx+i], cnt + 1)  # 여기서 idx+1이 data에서 이동하기때문에 idx가 4까지 가야함
            # 아무리 여기에다가 cnt-=1을 적어도 cnt에 영향미치지 않음!



for t in range(int(input())):
    data = list(map(int, input().split()))
    N = data.pop(0)
    cnt = 0
    k = data[0]
    data.append(0)  # idx가 마지막까지 도달해야함 -> ex. data=[2, 3, 1, 1, 0]
    mymin = 999999999

    bus(0, k, 0)

    print('#{} {}'.format(t+1, mymin))
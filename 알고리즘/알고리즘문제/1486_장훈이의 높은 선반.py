def top(idx, s):  # idx=0,1,2,3,4
    global mymin

    if idx < N and s < B:
        sum = s + data[idx]
        top(idx + 1, sum)  # idx가 4이면, idx+1은 5이다.
        if mymin > sum and sum >= B:
            mymin = sum
        top(idx + 1, s)  # 이제 idx=0인 경우에는 다 했기 때문에, idx=1부터 시작할 때를 찾아야함
        return mymin


for t in range(int(input())):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    mymin = 99999999999
    s = 0

    rs = top(0, 0) - B
    print('#{} {}'.format(t+1, rs))
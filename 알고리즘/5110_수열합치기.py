for t in range(int(input())):
    N, M = map(int, input().split())  # N: 수열의 길이, M: 수열의 갯수
    data = list(map(int, input().split()))
    # print(data)
    for M in range(M - 1):
        plus_data = list(map(int, input().split()))
        # print(plus_data)
        for i in range(len(data)):
            if data[i] > plus_data[0]:
                data[i:0] = plus_data
                # left_data = data[:i]
                # # print(left_data)
                # right_data = data[i:]
                # # print(right_data)
                # new_data = left_data + plus_data + right_data
                # data = new_data
                break
            if i == len(data) - 1:
                data += plus_data

    print('#{}'.format(t+1), end=' ')
    data.reverse()
    for k in range(10):
        print(data[k], end=' ')
    print()

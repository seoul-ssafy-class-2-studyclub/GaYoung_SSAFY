for t in range(int(input())):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    for m in range(M):
        idx, num = map(int, input().split())
        left_data = data[:idx]
        right_data = data[idx:]

        data_new = left_data + [num] + right_data
        data = data_new

    print('#{} {}'.format(t+1, data[L]))
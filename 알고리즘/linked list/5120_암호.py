for t in range(int(input())):
    N, M, K = map(int, input().split())
    data = [958, 386, 329, 498, 169, 778]
    start = 3
    first = 958
    # for k in range(K):
    start = start + M
    # if start <= len(data) - 2:
    #     data[start:0] = [data[start - 1] + data[start]]
    if start == len(data):
        data[start:0] = [data[start - 1] + first]
    # if start > len(data) - 1:
    #     start = start - len(data)
    #     data[start:0] = [data[start - 1] + data[start]]
    print(data)
    # data = data[::-1]
    #
    # print('#{}'.format(t + 1), end=' ')
    # if len(data) > 10:
    #     for i in range(10):
    #         print(data[i], end=' ')
    #     print()
    # else:
    #     for i in range(len(data)):
    #         print(data[i], end=' ')
    #     print()
for t in range(int(input())):   # 10
    n = int(input())  # 3
    data = list(map(int, input().split()))  # [3, 4, 2, 3, 4, 5]
    data_xy = []  # 두개씩 들어갈리스트
    for i in range(0, n*2, 2):
        data_xy.append((data[i], data[i+1]))  # [(3, 4), (2, 3), (4, 5)]
    result = []
    result += [data_xy.pop()]  # [(4, 5)]

    while len(data_xy) > 0:
        for k in data_xy:
            if result[0][0] == k[1]:
                result.insert(0, k)
                data_xy.remove(k)
            if result[-1][1] == k[0]:
                result.append(k)
                data_xy.remove(k)

    print(f'#{t+1}', end=' ')
    for j in result:
        print(f'{j[0]} {j[1]}', end=' ')
    print(' ')


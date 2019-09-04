# result = []
# def combination(arr, k):
#     if len(arr) == 2:
#         result.append(arr)
#         return result
#     else:
#         for idx in range(k + 1, len(data)):
#             combination(arr + [data[idx]], idx)


def danjo(x):
    a = x % 10
    x //= 10
    while x:
        if x % 10 > a:
            return False
        a = x % 10
        x //= 10
    return True


for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))

    flag = -1
    for i in range(N):
        for j in range(i+1, N):
            x = data[i] * data[j]
            if flag > x:
                continue
            elif danjo(x) == True and flag < x:
                flag = x

    print('#{} {}'.format(t+1, flag))

    # res = result[::-1]
    # for r in res:
    #     if flag != -1:
    #         break
    #     dan = r[0] * r[1]
    #     # print(dan)   # [8, 14, 20, 28, 40, 70]

    #     if dan // 10
    #     # for i in range(len(dan) - 1):
    #     #     if dan[i] <= dan[i + 1]:
    #     #         flag = dan
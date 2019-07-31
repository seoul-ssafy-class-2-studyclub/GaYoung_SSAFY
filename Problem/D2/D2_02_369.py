N = int(input())

if 10 <= N <= 1000:
    result = []
    for n in range(1, N + 1):  # 1~10까지 나열 -> int
        count = 0
        for i in str(n): # 1~10까지 나열 -> str
            if i in ['3', '6', '9']:
                # print(i)
                count += 1
                # print(count)
        if count > 0:
            result.append('-' * count)
        else:
            result.append(n)
    result_ans = ' '.join(map(str, result))
    print(result_ans)

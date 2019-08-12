for t in range(int(input())):
    N = int(input())
    result = []
    data = ''
    for n in range(N):
        alp, num = input().split()
        for i in range(int(num)):
            data += alp
            if len(data) == 10:
                result += [data]
                data = ''
    if data:
        result += [data]
    print('# %d' % (t+1))
    for k in result:
        print(k)

def jaegop(num, mul):
    if mul == 1:
        return num
    return num * jaegop(num, mul - 1)

for t in range(10):
    N = int(input())
    num, mul = map(int, input().split())
    print('#{} {}'.format(t+1, jaegop(num, mul)))

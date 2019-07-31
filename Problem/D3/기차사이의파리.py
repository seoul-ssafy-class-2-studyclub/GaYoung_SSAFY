T = int(input())
for t in range(1, T + 1):
    d, a, b, f = map(int, input().split())
    time = d / (a + b)  #  a + b 속력
    distance = time * f
    print('#{0} {1:.7f}'.format(t, distance))
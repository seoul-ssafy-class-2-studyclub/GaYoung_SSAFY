for t in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())
    sum_h = h1 + h2
    sum_m = m1 + m2
    if sum_m >= 60:
        sum_h += 1
        sum_m -= 60
    if sum_h >= 12:
        sum_h -= 12
    print('#{0} {1} {2}'.format(t+1, sum_h, sum_m))
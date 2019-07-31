T = int(input())

for t in range(1, T + 1):
    N = input()
    y = N[0:4]   # '2222'
    m = N[4:6]   # '02'
    d = N[6:]   # '28'

    if m == '01' or m == '03' or m == '05' or m == '07' or m == '08' or m == '10' or m == '12':
        if int(d) > 31:
            d = '-1'
    elif m == '04' or m == '06' or m == '09' or m == '11':
        if int(d) > 30:
            d = '-1'
    elif m == '02':
        if int(d) > 28:
            d = '-1'
    else:
        d = '-1'

    if d == '-1':
        print(f'#{d}')
    else:
        print(f'#{y}/{m}/{d}')
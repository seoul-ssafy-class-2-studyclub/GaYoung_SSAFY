a = int(input())
if a < 30:
    for k in range(0, a+1):
        if k <= a:
            print(2**k, end=' ')
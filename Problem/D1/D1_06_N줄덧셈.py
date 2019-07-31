a = int(input())
total = 0

if a <= 10000:
    while a > 0:
        total += a
        a -= 1
    print(total)
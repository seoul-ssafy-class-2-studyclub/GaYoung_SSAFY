n = int(input())
length = 0
for i in range(n//2 + 1, n + 1):   # i = 51, 52,,, 100
    num = [n, i]
    while num[-2] - num[-1] >= 0:
        num += [num[-2] - num[-1]]
        if num[-2] - num[-1] < 0:
            break

    if len(num) > length:
        length = len(num)
        result = num

print(length)
for k in result:
    print(k, end=' ')

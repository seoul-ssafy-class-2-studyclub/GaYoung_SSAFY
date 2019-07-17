T = int(input())

for t in range(1, T + 1):
    total = 0
    sum = []
    num = map(int, input().split())
    for k in num:  # 3 17 1 39 8 41 2 32 99 2
        total += k
        sum += [k]
        mean = total / len(sum)
    print(f'#{t} {round(mean)}')
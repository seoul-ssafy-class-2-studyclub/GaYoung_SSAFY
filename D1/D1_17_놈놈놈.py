T = int(input())

for t in range(1, T + 1):
    num = list(map(int, input().split()))  # [3 8]
    for k in num:  # 3  8
        if num[0] < num[1]:
            result = '<'
        elif num[0] == num[1]:
            result = '='
        else:
            result = '>'            
    print(f'#{t} {result}')


T = int(input())

for t in range(1, T + 1):
    num = list(map(int, input().split()))  #[3, 17, 1, 39, 8, 41, 2, 32, 99, 2]
    max_num = max(num)
    print(f'#{t} {max_num}')
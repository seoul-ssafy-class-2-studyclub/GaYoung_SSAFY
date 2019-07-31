T = int(input())

for t in range(1, T + 1):
    num = list(map(int, input().split())) #list는 왜 들어갈까?
    a = num[0] // num[1]
    b = num[0] % num[1]
    print(f'#{t} {a} {b}')
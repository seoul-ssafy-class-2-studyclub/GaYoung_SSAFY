T = int(input())

for t in range(1, T + 1): # #1, #2, #3 으로 뜨는 것
    result = 0
    num = map(int, input().split())  # 3 17 1 39 ...
    for k in num:
        if k % 2 == 1:
            result += k
    print(f'#{t} {result}')



## 다른 방법
T = int(input())

for t in range(1, T + 1): # #1, #2, #3 으로 뜨는 것
    result = 0
    num = list(map(int, input().split()))  # 3 17 1 39 ...
    for k in range(0, len(num)):  # why? len
        if num[k] % 2 == 1:
            result += num[k]
    print(f'#{t} {result}')
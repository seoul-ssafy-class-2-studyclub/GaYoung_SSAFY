# 2~999 소수찾기
result = []
for i in range(2, 1000):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check == True:
        result.append(i)  # [2, 3, 5, 7, 11,,]

# 소수로 더해지는 경우의 수 찾기
for t in range(int(input())):  # 3
    N = int(input())  # 7 \n 11 \n 25
    answer = []
    count = 0
    for x in range(len(result)):
        for y in range(x, len(result)):
            for z in range(y, len(result)):
                if result[x] + result[y] + result[z] == N:
                    answer.append([result[x], result[y], result[z]])
    print(f'#{t+1} {len(answer)}')
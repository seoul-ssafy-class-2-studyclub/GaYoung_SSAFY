result = []
for t in range(int(input())):
    N = int(input())
    numbers = [0] * N
    for i in range(N):
        numbers[i] = input()

    numbers.sort()

    flag = False
    for i in range(N - 1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            flag = True
            break

    if flag:
        result.append('NO')
    else:
        result.append('YES')

print('\n'.join(result))

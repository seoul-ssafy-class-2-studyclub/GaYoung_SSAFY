def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def pascal(x):
    if x == 1:
        print(1)
    else:
        pascal(x - 1)
        for i in range(x):
            number = int(fac(x - 1) / (fac(i) * fac(x - 1 - i)))
            if i == x - 1:
                print(number)
            else:
                print(number, end=' ')

for t in range(int(input())):
    N = int(input())

    print('#{}'.format(t + 1))
    pascal(N)

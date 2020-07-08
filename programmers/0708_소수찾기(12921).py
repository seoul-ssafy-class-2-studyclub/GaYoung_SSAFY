def solution(n):
    numbers = set(i for i in range(2, n+1))
    for i in range(2, n + 1):
        if i in numbers:
            numbers -= set(j for j in range(2 * i, n + 1, i))
    print(numbers)
    return len(numbers)

n=5
print(solution(n))
def solution(n):
    numbers = list(str(n))
    numbers.reverse()

    print(numbers)

    return numbers

n = 123745
print(solution(n))
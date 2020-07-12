N = 123

def solution(n):
    numbers = list(str(n))
    ans = 0
    for i in numbers:
        ans += int(i)

    return ans

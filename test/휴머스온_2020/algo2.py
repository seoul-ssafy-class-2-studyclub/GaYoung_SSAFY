def solution(A, S):
    answer = 2

    return answer


A = [1, 1, 1, 1]
S = 3

total = []

for i in range(len(A)):
    start, end = i, i
    res = A[start]
    while True:
        if end == len(A):
            break

        if res == S:
            answer = [start, end]
            total.append(answer)
            break

        elif res < S:
            res += A[end]
        end += 1

print(len(total))
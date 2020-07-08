def solution(strings, n):

    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    print(strings)
    strings = sorted(strings)
    print('sort')
    print(strings)

    answer = []
    for i in strings:
        answer.append(i[1:])

    return answer

# strings = ['sun', 'bed', 'car']
# n=1

strings = ['abce', 'abcd', 'cdx']
n = 2

print(solution(strings,n))
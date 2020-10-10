# name = 'JEROEN'
name = 'JAN'
# name = 'JAZ'
# name = 'BBBAAAB'
# name = 'ABABAAAAABA'


def count(i):  # M, N = 12
    if i == 'Z':
        return 1

    else:
        a = ord(i) - ord('A')
        z = ord('Z') - ord(i) + 1
        if a < z + 1:
            return a
        else:
            return z

def solution(name):
    name = list(name)

    if name == ['A'] * len(name):
        return 0

    answer = 0
    idx = 0
    while True:
        left, right = 1, 1

        if name[idx] != 'A':
            answer += count(name[idx])
        name[idx] = 'A'
        print(name)
        print('answer')
        print(answer)
        if name == ['A'] * len(name):
            break

        for i in range(1, len(name)):
            if name[idx + i] == 'A':
                right += 1
            else:
                break

        for i in range(1, len(name)):
            if name[idx - i] == 'A':
                left += 1
            else:
                break

        if left < right:
            print('left')
            idx -= left
            answer += left

        else:
            print('right')
            idx += right
            answer += right

    return answer
print(solution(name))
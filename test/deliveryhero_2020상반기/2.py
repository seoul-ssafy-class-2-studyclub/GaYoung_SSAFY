def solution(S):
    ls = S.split()

    stack = [ls[0]]
    for i in range(1, len(ls)):
        if ls[i] == 'DUP':
            stack.append(stack[-1])
        elif ls[i] == 'POP':
            stack.pop()
        elif ls[i] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(a) + int(b)))
        elif ls[i] == '-':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a) - int(b)))
            else:
                return -1

        else:
            stack.append(ls[i])

    answer = stack[-1]

    return int(answer)


# S = '13 DUP 4 POP 5 DUP + DUP + -'
S = '3 DUP 5 - -'
print(solution(S))
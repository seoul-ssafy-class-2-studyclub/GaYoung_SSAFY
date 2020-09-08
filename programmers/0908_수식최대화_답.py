from itertools import permutations

def calculation(a, b, c):
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c


def solution(expression):
    answer = 0

    # 1번
    expression_list = []
    susic_list = ['+', '-', '*']
    str_stack = ''
    for i in range(len(expression)):
        if expression[i] in susic_list:
            expression_list.append(int(str_stack))
            str_stack = ''
            expression_list.append(expression[i])
        else:
            str_stack += expression[i]
    expression_list.append(int(str_stack))
    print(expression_list)

    # 2번 괜히 itertools 한번 연습해보기
    susic_permu = permutations(susic_list, 3)

    # 3번
    for susic_order in susic_permu:
        copied_expression = expression_list[:]
        for susic in susic_order:
            flag = True

            while flag:
                flag = False
                for i in range(len(copied_expression)):
                    if copied_expression[i] == susic:
                        a = copied_expression.pop(i - 1)
                        b = copied_expression.pop(i - 1)
                        c = copied_expression.pop(i - 1)
                        d = calculation(a, b, c)
                        copied_expression.insert(i - 1, d)
                        flag = True
                        break
        answer = max(abs(copied_expression[0]), answer)
    return answer

print(solution(expression='100-200*300-500+20'))
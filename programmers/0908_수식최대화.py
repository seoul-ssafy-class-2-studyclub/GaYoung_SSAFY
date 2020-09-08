from itertools import permutations

def solution(expression):
    numbers = []
    number = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            number += expression[i]
        else:
            numbers.append(int(number))
            numbers.append(expression[i])
            number = ''
    numbers.append(int(number))
    print(numbers)

    temp = ['+', '-', '*']
    perm = list(permutations(temp, 3))

    answer = 0
    for per in perm:
        mymax = 0
        copy_numbers = numbers[:]
        for i in per:
            flag = True
            '''
            1. flag로 두고 for j를 돌려야
            [100, '-', 200, '*', 300, '-', 500, '+', 20]
            -> [100, '-', 200, '*', 300, '-', 520]
            에서 끝나지 않을 수 있다.

            2. break안하면 index error

            3.  while문, flag없애면 그냥 앞에서부터 진행한다.
            '''
            while flag:
                flag = False
                for j in range(len(copy_numbers) - 1):
                    if copy_numbers[j] == i:
                        num1 = copy_numbers.pop(j - 1)
                        oper = copy_numbers.pop(j - 1)
                        num2 = copy_numbers.pop(j - 1)
                        plus = calculate(num1, num2, oper)
                        copy_numbers.insert(j - 1, plus)
                        flag = True
                        break

        mymax = abs(copy_numbers[0])

        if answer < mymax:
            answer = mymax

    return answer


def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2


expression = '100-200*300-500+20'
# expression = '50*6-3*2'
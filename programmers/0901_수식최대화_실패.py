from itertools import permutations

expression = '100-200*300-500+20'
# expression = '50*6-3*2'

def solution():


    return 0


operation = ['+', '-', '*']
can = list(permutations(operation, 3))  # [('+', '-', '*'), ('+', '*', '-'),,,]

numbers = []
oper = []
num = ''
for i in range(len(expression)):
    if expression[i].isdigit():
        num += expression[i]
    else:
        numbers.append(int(num))
        oper.append(expression[i])
        num = ''
numbers.append(int(num))

mymax = 0
# for c in can:

numbers_copy = numbers[:]
oper_copy = oper[:]

arr = []
c = ['*', '+', '-']
for i in range(len(c)):
    for j in range(len(oper)):

        if c[i] == oper[j]:
            num1, num2 = numbers_copy[j], numbers_copy[j+1]
            if c[i] == '+':
                arr.append(num1+num2)
            elif c[i] == '-':
                arr.append(num1-num2)

            elif c[i] == '*':
                arr.append(num1*num2)
        print(numbers_copy)
        numbers_copy = arr
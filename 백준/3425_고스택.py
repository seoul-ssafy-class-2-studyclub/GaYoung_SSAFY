def num_x(x):
    number.append(x)

def pop(arr):
    if len(arr) < 1:
        return 'ERROR'
    number.pop()

def inv(arr):
    arr[-1] = -arr[-1]

def dup(arr):
    number.append(arr[-1])

def swp(arr):
    if len(arr) <= 1:
        return 'ERROR'
    arr[-1], arr[-2] = arr[-2], arr[-1]

def add(arr):
    if len(arr) <= 1:
        return 'ERROR'
    ssum = arr.pop() + arr.pop()
    if abs(ssum) > 1e9:
        return 'ERROR'
    number.append(ssum)

def sub(arr):
    if len(arr) <= 1:
        return 'ERROR'
    minus = arr[-2] - arr[-1]
    if abs(minus) > 1e9:
        return 'ERROR'
    number.append(minus)

def mul(arr):
    if len(arr) <= 1:
        return 'ERROR'
    multi = arr.pop(0) * arr.pop(0)
    if abs(multi) > 1e9:
        return 'ERROR'
    number.append(multi)

def div(arr):
    if len(arr) <= 1 or arr[-1] == 0:
        return 'ERROR'
    x = number.pop()
    y = number.pop()
    if y > 0:
        if x > 0:
            divv = y // x
        else:
            divv = -(y // abs(-x))
    else:
        if x > 0:
            divv = -(y // x)
        else:
            divv = abs(-y) // abs(-x)
    if abs(divv) > 1e9:
        return 'ERROR'
    number.append(divv)

def mod(arr):
    if len(arr) <= 1 or arr[-1] == 0:
        return 'ERROR'
    x = number.pop()
    y = number.pop()
    if y > 0:
        if x > 0:
            modd = y % x
        else:
            modd = y % abs(-x)
    else:
        if x > 0:
            modd = -(abs(-y) % x)
        else:
            modd = -(abs(-y) % abs(-x))
    if abs(modd) > 1e9:
        return 'ERROR'
    number.append(modd)



flag = False
while True:
    operator = []
    while True:
        oper = input()
        operator.append(oper)
        if oper == 'END':
            break
        if oper == 'QUIT':
            flag = True
            break

    if flag:
        break

    N = int(input())

    for i in range(N):
        number = []
        num = int(input())
        number.append(num)

        # [2, 7]에서 num_x로 스택의 가장 위에 저장하는 것이라면 num 8이면 [2, 7, 8]이 된다
        # 첫번째 숫자는 number.pop()할 때 나오는 것 -> 즉, 8!
        for o in operator:
            if o[:3] == 'NUM':
                a = int(o[4:])
                num_x(a)
            elif o[:3] == 'POP':
                pop(number)
            elif o[:3] == 'INV':
                inv(number)
            elif o[:3] == 'DUP':
                dup(number)
            elif o[:3] == 'SWP':
                swp(number)
            elif o[:3] == 'ADD':
                add(number)
            elif o[:3] == 'SUB':
                sub(number)
            elif o[:3] == 'MUL':
                mul(number)
            elif o[:3] == 'DIV':
                div(number)
            elif o[:3] == 'MOD':
                mod(number)

        if len(number) == 1:
            print(number[0])
        if len(number) != 1:
            print('ERROR')
    print()
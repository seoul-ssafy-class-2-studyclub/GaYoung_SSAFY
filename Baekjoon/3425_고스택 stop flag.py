def num_x(x):
    number.append(x)
def pop(arr):
    global stop
    if len(arr) < 1:
        stop = True
        return
    number.pop()
def inv(arr):
    global stop
    if len(arr) == 0:
        stop = True
        return
    arr[-1] = -arr[-1]
def dup(arr):
    global stop
    if len(arr) == 0:
        stop = True
        return
    number.append(arr[-1])
def swp(arr):
    global stop
    if len(arr) <= 1:
        stop = True
        return
    arr[-1], arr[-2] = arr[-2], arr[-1]
def add(arr):
    global stop
    if len(arr) <= 1:
        stop = True
        return
    ssum = arr.pop() + arr.pop()
    if abs(ssum) > 1e9:
        stop = True
        return
    number.append(ssum)
def sub(arr):
    global stop
    if len(arr) <= 1:
        stop = True
        return
    x = arr.pop()
    y = arr.pop()
    minus = y - x
    if abs(minus) > 1e9:
        stop = True
        return
    number.append(minus)
def mul(arr):
    global stop
    if len(arr) <= 1:
        stop = True
        return
    multi = arr.pop() * arr.pop()
    if abs(multi) > 1e9:
        stop = True
        return
    number.append(multi)
def div(arr):
    global stop
    if len(arr) <= 1 or arr[-1] == 0:
        stop = True
        return
    x = number.pop()
    y = number.pop()
    a = 0 # 부호
    # 계산
    if x < 0:
        a += 1
    if y < 0:
        a += 1
    divv = abs(y) // abs(x)
    if a == 1:
        divv = -divv

    if abs(divv) > 1e9:
        stop = True
        return
    number.append(divv)

def mod(arr):
    global stop
    if len(arr) <= 1 or arr[-1] == 0:
        stop = True
        return
    x = number.pop()
    y = number.pop()
    modd = abs(y) % abs(x)

    if y < 0:
        modd = -modd

    if abs(modd) > 1e9:
        stop = True
        return
    number.append(modd)


flag = False
while True:
    operator = []
    while True:
        oper = input()
        # END가 QUIT보다 먼저 적힌다면 END해서 break되면 밑에 QUIT로 가지 못함!!
        if oper == 'QUIT':
            flag = True
            break

        if oper == 'END':
            break

        operator.append(oper)
    if flag:
        break
    N = int(input())

    for i in range(N):
        stop = False
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
                if stop:
                    break
            elif o[:3] == 'INV':
                inv(number)
                if stop:
                    break
            elif o[:3] == 'DUP':
                dup(number)
                if stop:
                    break
            elif o[:3] == 'SWP':
                swp(number)
                if stop:
                    break
            elif o[:3] == 'ADD':
                add(number)
                if stop:
                    break
            elif o[:3] == 'SUB':
                sub(number)
                if stop:
                    break
            elif o[:3] == 'MUL':
                mul(number)
                if stop:
                    break
            elif o[:3] == 'DIV':
                div(number)
                if stop:
                    break
            elif o[:3] == 'MOD':
                mod(number)
                if stop:
                    break

        if stop or len(number) != 1:
            print('ERROR')
        elif len(number) == 1:
            print(number[0])

    print()
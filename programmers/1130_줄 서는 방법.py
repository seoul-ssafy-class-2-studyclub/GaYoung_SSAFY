n, k = 3, 5

import math

answer = []
num = [i for i in range(1, n+1)]
print(num)
while n:
    temp = math.factorial(n) // n  # 한번에 몇개씩의 값이 있을 수 있는지
    mok, na = divmod(k, temp)  # 2 1
    print(mok, na)
    # if na == 0:
    #     answer.append(num.pop(mok-1))
    #     print('na=0')
    # else:
    #     answer.append(num.pop(mok))
    #     print('na!=0')
    n -= 1


def solution(n, k):
    answer = []
    numberList = [i for i in range(1, n+1)]
    while (n != 0):
        temp = math.factorial(n) // n # 한개에 몇개씩의 값이 있을지 알 수 잇음.
        index = k // temp
        k = k % temp
        # print(index, k)
        if k == 0:
            answer.append(numberList.pop(index-1))
            # print('1')
        else:
            answer.append(numberList.pop(index))
            # print('2')

        n -= 1
    # print(answer)
    return answer
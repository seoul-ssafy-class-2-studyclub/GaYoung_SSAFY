'''
** 점수는 0에서 10 사이의 정수이다.
'''

# solution2보다 0.01초 정도 빠르다
# 10을 다른 숫자나 문자로 치환 후 진행
def solution1(dartResult):

    bonus = {'S': 1, 'D': 2, 'T': 3}
    options = ['*', '#']
    answer = []

    dartResult = dartResult.replace('10', 't')
    for i in range(len(dartResult)):
        if dartResult[i] in bonus:
            if dartResult[i - 1] == 't':
                answer.append(10 ** bonus[dartResult[i]])
            else:
                # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
                # dartResult[i-1]가 str이므로 int ** int를 해줘야함
                answer.append(int(dartResult[i - 1]) ** bonus[dartResult[i]])

        if dartResult[i] in options:
            if dartResult[i] == '*':
                if len(answer) == 1:
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            else:
                answer[-1] *= (-1)

    res = 0
    for ans in answer:
        res += ans

    return res



# 10을 그대로 두고 진행
def solution2(dartResult):

    bonus = {'S': 1, 'D': 2, 'T': 3}
    options = ['*', '#']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = []

    for i in range(len(dartResult)):
        if dartResult[i] in bonus:
            if dartResult[i - 2:i] == '10':
                answer.append(10 ** bonus[dartResult[i]])

            elif dartResult[i-1] in numbers:
                # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
                # dartResult[i-1]가 str이므로 int ** int를 해줘야함
                answer.append(int(dartResult[i - 1]) ** bonus[dartResult[i]])

        if dartResult[i] in options:
            if dartResult[i] == '*':
                if len(answer) == 1:
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            else:
                answer[-1] *= (-1)
    print(answer)
    res = 0
    for ans in answer:
        res += ans

    return res


# dartResult = '1S2D*3T'
dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
# dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
# dartResult = '1D2S3T*'

print(solution2(dartResult))